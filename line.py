import abc
from typing import Protocol, Any, Union, runtime_checkable

from constants import MAX_LINE, MIN_LINE


@runtime_checkable
class ReturnStatisticsProtocol(Protocol):
    def get_statistics(self,
                       clients_attended: list[Any]) -> (
            dict[str, Union[str, int, list[Any]]]
    ): ...


class Line(metaclass=abc.ABCMeta):
    code: int = 0
    line: list[str] = []
    clients_attended: list[str] = []
    current_password: str = ""

    @abc.abstractmethod
    def generate_current_password(self) -> None:
        ...

    def update_line(self) -> None:
        self.increment_line()
        self.generate_current_password()
        self.line.append(self.current_password)

    def increment_line(self) -> None:
        if self.code > MAX_LINE:
            self.code = MIN_LINE
        else:
            self.code += 1

    def call_client(self, desk_number: int) -> str:
        current_client = self.line.pop(0)
        self.clients_attended.append(current_client)
        return f"{current_client} on {desk_number}"

    def statistics(self, return_statistics: ReturnStatisticsProtocol) -> (
            dict[str, Union[str, int, list[Any]]]
    ):

        return return_statistics.get_statistics(self.clients_attended)
