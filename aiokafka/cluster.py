import collections
import logging
import time
from typing import Any, Dict, Optional, cast

from kafka.cluster import ClusterMetadata as BaseClusterMetadata
from kafka.protocol.metadata import (
    BrokerMetadata_v1,
    MetadataResponse,
    MetadataResponse_v1,
    TopicMetadata_v1,
)

from aiokafka import errors as Errors
from aiokafka.structs import BrokerMetadata, PartitionMetadata, TopicPartition

log = logging.getLogger(__name__)


class ClusterMetadata(BaseClusterMetadata):
    def __init__(self, *args: Any, **kw: Any):
        super().__init__(*args, **kw)
        self._coordinators: Dict[int, "BrokerMetadata"] = {}
        self._coordinator_by_key: Dict[str, int] = {}

    def coordinator_metadata(self, node_id: int) -> Optional["BrokerMetadata"]:
        return self._coordinators.get(node_id)

    def add_coordinator(
        self,
        node_id: int,
        host: str,
        port: int,
        rack: Optional[str] = None,
        *,
        purpose: str
    ) -> None:
        """Keep track of all coordinator nodes separately and remove them if
        a new one was elected for the same purpose (For example group
        coordinator for group X).
        """
        if purpose in self._coordinator_by_key:
            old_id = self._coordinator_by_key.pop(purpose)
            del self._coordinators[old_id]

        self._coordinators[node_id] = BrokerMetadata(node_id, host, port, rack)
        self._coordinator_by_key[purpose] = node_id

    def update_metadata(self, metadata: MetadataResponse) -> None:
        """Update cluster state given a MetadataResponse.

        Arguments:
            metadata (MetadataResponse): broker response to a metadata request

        Returns: None
        """

        if not metadata.brokers:
            log.warning("No broker metadata found in MetadataResponse")

        _new_brokers = {}
        for broker in metadata.brokers:
            if metadata.API_VERSION == 0:
                node_id, host, port = broker
                rack = None
            else:
                # mypy doesn't recognize that broker is a 4-tuple, hence ignore it here
                node_id, host, port, rack = cast(
                    BrokerMetadata_v1, broker
                )  # type: ignore
            _new_brokers.update({node_id: BrokerMetadata(node_id, host, port, rack)})

        if metadata.API_VERSION == 0:
            _new_controller = None
        else:
            _new_controller = _new_brokers.get(
                cast(MetadataResponse_v1, metadata).controller_id
            )

        _new_partitions: Dict[str, Dict[int, "PartitionMetadata"]] = {}
        _new_broker_partitions = collections.defaultdict(set)
        _new_unauthorized_topics = set()
        _new_internal_topics = set()

        for topic_data in metadata.topics:
            if metadata.API_VERSION == 0:
                error_code, topic, partitions = topic_data
                is_internal = False
            else:
                # Cast to MetadataResponse_v1 since other versions subclass it
                error_code, topic, is_internal, partitions = cast(
                    TopicMetadata_v1, topic_data
                )  # type: ignore
            if is_internal:
                _new_internal_topics.add(topic)
            error_type = Errors.for_code(error_code)
            if error_type is Errors.NoError:
                _new_partitions[topic] = {}
                for p_error, partition, leader, replicas, isr in partitions:
                    _new_partitions[topic][partition] = PartitionMetadata(
                        topic=topic,
                        partition=partition,
                        leader=leader,
                        replicas=replicas,
                        isr=isr,
                        error=p_error,
                    )
                    if leader != -1:
                        _new_broker_partitions[leader].add(
                            TopicPartition(topic, partition)
                        )

            elif error_type is Errors.LeaderNotAvailableError:
                log.warning(
                    "Topic %s is not available during auto-create" " initialization",
                    topic,
                )
            elif error_type is Errors.UnknownTopicOrPartitionError:
                log.error("Topic %s not found in cluster metadata", topic)
            elif error_type is Errors.TopicAuthorizationFailedError:
                log.error("Topic %s is not authorized for this client", topic)
                _new_unauthorized_topics.add(topic)
            elif error_type is Errors.InvalidTopicError:
                log.error("'%s' is not a valid topic name", topic)
            else:
                log.error("Error fetching metadata for topic %s: %s", topic, error_type)

        with self._lock:
            self._brokers = _new_brokers
            self.controller = _new_controller
            self._partitions = _new_partitions
            self._broker_partitions = _new_broker_partitions
            self.unauthorized_topics = _new_unauthorized_topics
            self.internal_topics = _new_internal_topics

        now = time.time() * 1000
        self._last_refresh_ms = now
        self._last_successful_refresh_ms = now

        log.debug("Updated cluster metadata to %s", self)

        for listener in self._listeners:
            listener(self)
