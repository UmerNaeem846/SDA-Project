from typing import Protocol, List, Any, runtime_checkable


@runtime_checkable
class DataSink(Protocol):
    """
    Outbound Abstraction.
    Core calls this to send processed data outward.
    """

    def write(self, records: List[dict]) -> None:
        ...


class PipelineService(Protocol):
    """
    Inbound Abstraction.
    Input modules call this to send raw data to Core.
    """

    def execute(self, raw_data: List[Any]) -> None:
        ...