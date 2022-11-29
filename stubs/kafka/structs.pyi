from typing import NamedTuple, Optional

from kafka.errors import KafkaError

class TopicPartition(NamedTuple):
    topic: str
    partition: int

class BrokerMetadata(NamedTuple):
    nodeId: int
    host: str
    port: int
    rack: Optional[str]

class PartitionMetadata(NamedTuple):
    topic: str
    partition: int
    leader: int
    replicas: list[int]
    isr: list[int]
    error: int

class OffsetAndMetadata(NamedTuple):
    offset: int
    metadata: str
