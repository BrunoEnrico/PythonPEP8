from typing import Union, Any


class ResumedStatistics:
    def __init__(self, day: str, agency: int) -> None:
        self.day = day
        self.agency = agency

    def get_statistics(self, clients_attended: list[Any]) -> (
            dict[str, Union[str, int, list[Any]]]
    ):
        return {
            f"{self.agency} -- {self.day}": len(clients_attended)
        }
