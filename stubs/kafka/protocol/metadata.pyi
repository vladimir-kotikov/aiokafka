from typing import List, NamedTuple, Sequence, Union

class BrokerMetadata_v0(NamedTuple):
    node_id: int
    host: str
    port: int

class BrokerMetadata_v1(BrokerMetadata_v0):
    node_id: int
    host: str
    port: int
    rack: str

class PartitionMetadata_v0(NamedTuple):
    error_code: int
    partition: int
    leader: int
    replicas: list[int]
    isr: list[int]

class PartitionMetadata_v5(PartitionMetadata_v0):
    offline_replicas: list[int]

class TopicMetadata_v0(NamedTuple):
    error_code: int
    topic: str
    partitions: Sequence[PartitionMetadata_v0]

class TopicMetadata_v1(TopicMetadata_v0):
    error_code: int
    topic: str
    is_internal: bool
    partitions: Sequence[PartitionMetadata_v0]

class TopicMetadata_v5(TopicMetadata_v1):
    partitions: Sequence[PartitionMetadata_v5]

class MetadataResponse_v0:
    API_KEY = 3
    API_VERSION = 0

    brokers: Sequence[BrokerMetadata_v0]
    topics: Sequence[TopicMetadata_v0]

class MetadataResponse_v1(MetadataResponse_v0):
    API_KEY = 3
    API_VERSION = 1

    brokers: Sequence[BrokerMetadata_v1]
    controller_id: int
    topics: Sequence[TopicMetadata_v1]

class MetadataResponse_v2(MetadataResponse_v1):
    API_KEY = 3
    API_VERSION = 2

    cluster_id: str

class MetadataResponse_v3(MetadataResponse_v2):
    API_KEY = 3
    API_VERSION = 3

    throttle_time_ms: int

class MetadataResponse_v4(MetadataResponse_v3):
    API_KEY = 3
    API_VERSION = 4

class MetadataResponse_v5(MetadataResponse_v4):
    API_KEY = 3
    API_VERSION = 5

    topics: Sequence[TopicMetadata_v5]

class MetadataRequest_v0:
    topics: List[str]

class MetadataRequest_v1(MetadataRequest_v0):
    pass

class MetadataRequest_v2(MetadataRequest_v0):
    pass

class MetadataRequest_v3(MetadataRequest_v0):
    pass

class MetadataRequest_v4(MetadataRequest_v0):
    allow_auto_topic_creation: bool

class MetadataRequest_v5(MetadataRequest_v4):
    pass

MetadataRequest = Union[
    MetadataRequest_v1,
    MetadataRequest_v2,
    MetadataRequest_v3,
    MetadataRequest_v4,
    MetadataRequest_v5,
]
MetadataResponse = Union[
    MetadataResponse_v0,
    MetadataResponse_v1,
    MetadataResponse_v2,
    MetadataResponse_v3,
    MetadataResponse_v4,
    MetadataResponse_v5,
]
