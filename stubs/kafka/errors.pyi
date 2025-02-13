from typing import Any, Union

class KafkaError(RuntimeError):
    retriable: bool
    invalid_metadata: bool

class IllegalStateError(KafkaError): ...
class IllegalArgumentError(KafkaError): ...

class NoBrokersAvailable(KafkaError):
    retriable: bool
    invalid_metadata: bool

class NodeNotReadyError(KafkaError):
    retriable: bool

class KafkaProtocolError(KafkaError):
    retriable: bool

class CorrelationIdError(KafkaProtocolError):
    retriable: bool

class Cancelled(KafkaError):
    retriable: bool

class TooManyInFlightRequests(KafkaError):
    retriable: bool

class StaleMetadata(KafkaError):
    retriable: bool
    invalid_metadata: bool

class MetadataEmptyBrokerList(KafkaError):
    retriable: bool

class UnrecognizedBrokerVersion(KafkaError): ...
class IncompatibleBrokerVersion(KafkaError): ...

class CommitFailedError(KafkaError):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class AuthenticationMethodNotSupported(KafkaError): ...

class AuthenticationFailedError(KafkaError):
    retriable: bool

class BrokerResponseError(KafkaError):
    errno: Union[int, None]
    message: Union[str, None]
    description: Union[str, None]

class NoError(BrokerResponseError):
    errno: int
    message: str
    description: str

class UnknownError(BrokerResponseError):
    errno: int
    message: str
    description: str

class OffsetOutOfRangeError(BrokerResponseError):
    errno: int
    message: str
    description: str

class CorruptRecordException(BrokerResponseError):
    errno: int
    message: str
    description: str

InvalidMessageError = CorruptRecordException

class UnknownTopicOrPartitionError(BrokerResponseError):
    errno: int
    message: str
    description: str
    retriable: bool
    invalid_metadata: bool

class InvalidFetchRequestError(BrokerResponseError):
    errno: int
    message: str
    description: str

class LeaderNotAvailableError(BrokerResponseError):
    errno: int
    message: str
    description: str
    retriable: bool
    invalid_metadata: bool

class NotLeaderForPartitionError(BrokerResponseError):
    errno: int
    message: str
    description: str
    retriable: bool
    invalid_metadata: bool

class RequestTimedOutError(BrokerResponseError):
    errno: int
    message: str
    description: str
    retriable: bool

class BrokerNotAvailableError(BrokerResponseError):
    errno: int
    message: str
    description: str

class ReplicaNotAvailableError(BrokerResponseError):
    errno: int
    message: str
    description: str

class MessageSizeTooLargeError(BrokerResponseError):
    errno: int
    message: str
    description: str

class StaleControllerEpochError(BrokerResponseError):
    errno: int
    message: str
    description: str

class OffsetMetadataTooLargeError(BrokerResponseError):
    errno: int
    message: str
    description: str

class StaleLeaderEpochCodeError(BrokerResponseError):
    errno: int
    message: str

class GroupLoadInProgressError(BrokerResponseError):
    errno: int
    message: str
    description: str
    retriable: bool

class GroupCoordinatorNotAvailableError(BrokerResponseError):
    errno: int
    message: str
    description: str
    retriable: bool

class NotCoordinatorForGroupError(BrokerResponseError):
    errno: int
    message: str
    description: str
    retriable: bool

class InvalidTopicError(BrokerResponseError):
    errno: int
    message: str
    description: str

class RecordListTooLargeError(BrokerResponseError):
    errno: int
    message: str
    description: str

class NotEnoughReplicasError(BrokerResponseError):
    errno: int
    message: str
    description: str
    retriable: bool

class NotEnoughReplicasAfterAppendError(BrokerResponseError):
    errno: int
    message: str
    description: str
    retriable: bool

class InvalidRequiredAcksError(BrokerResponseError):
    errno: int
    message: str
    description: str

class IllegalGenerationError(BrokerResponseError):
    errno: int
    message: str
    description: str

class InconsistentGroupProtocolError(BrokerResponseError):
    errno: int
    message: str
    description: str

class InvalidGroupIdError(BrokerResponseError):
    errno: int
    message: str
    description: str

class UnknownMemberIdError(BrokerResponseError):
    errno: int
    message: str
    description: str

class InvalidSessionTimeoutError(BrokerResponseError):
    errno: int
    message: str
    description: str

class RebalanceInProgressError(BrokerResponseError):
    errno: int
    message: str
    description: str

class InvalidCommitOffsetSizeError(BrokerResponseError):
    errno: int
    message: str
    description: str

class TopicAuthorizationFailedError(BrokerResponseError):
    errno: int
    message: str
    description: str

class GroupAuthorizationFailedError(BrokerResponseError):
    errno: int
    message: str
    description: str

class ClusterAuthorizationFailedError(BrokerResponseError):
    errno: int
    message: str
    description: str

class InvalidTimestampError(BrokerResponseError):
    errno: int
    message: str
    description: str

class UnsupportedSaslMechanismError(BrokerResponseError):
    errno: int
    message: str
    description: str

class IllegalSaslStateError(BrokerResponseError):
    errno: int
    message: str
    description: str

class UnsupportedVersionError(BrokerResponseError):
    errno: int
    message: str
    description: str

class TopicAlreadyExistsError(BrokerResponseError):
    errno: int
    message: str
    description: str

class InvalidPartitionsError(BrokerResponseError):
    errno: int
    message: str
    description: str

class InvalidReplicationFactorError(BrokerResponseError):
    errno: int
    message: str
    description: str

class InvalidReplicationAssignmentError(BrokerResponseError):
    errno: int
    message: str
    description: str

class InvalidConfigurationError(BrokerResponseError):
    errno: int
    message: str
    description: str

class NotControllerError(BrokerResponseError):
    errno: int
    message: str
    description: str
    retriable: bool

class InvalidRequestError(BrokerResponseError):
    errno: int
    message: str
    description: str

class UnsupportedForMessageFormatError(BrokerResponseError):
    errno: int
    message: str
    description: str

class PolicyViolationError(BrokerResponseError):
    errno: int
    message: str
    description: str

class SecurityDisabledError(BrokerResponseError):
    errno: int
    message: str
    description: str

class NonEmptyGroupError(BrokerResponseError):
    errno: int
    message: str
    description: str

class GroupIdNotFoundError(BrokerResponseError):
    errno: int
    message: str
    description: str

class KafkaUnavailableError(KafkaError): ...
class KafkaTimeoutError(KafkaError): ...

class FailedPayloadsError(KafkaError):
    payload: Any
    def __init__(self, payload: Any, *args: Any) -> None: ...

class KafkaConnectionError(KafkaError):
    retriable: bool
    invalid_metadata: bool

class ProtocolError(KafkaError): ...
class UnsupportedCodecError(KafkaError): ...
class KafkaConfigurationError(KafkaError): ...
class QuotaViolationError(KafkaError): ...

class AsyncProducerQueueFull(KafkaError):
    failed_msgs: Any
    def __init__(self, failed_msgs: Any, *args: Any) -> None: ...

kafka_errors: dict[int, BrokerResponseError]

def for_code(error_code: int) -> BrokerResponseError: ...
def check_error(response: Exception) -> None: ...
