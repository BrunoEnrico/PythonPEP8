from typing import Union, Any


class DetailedStatistics:
    def __init__(self, day: str, agency: int) -> None:
        self.day = day
        self.agency = agency

    def get_statistics(self, clients_attended: list[Any]) -> (
        dict[str, Union[str, int, list[Any], int]]
    ):
        statistics: dict[str, Union[str, int, list[Any], int]] = {
            "day": self.day,
            "agency": self.agency,
            "clients_attended": clients_attended,
            "amount_clients_attended": len(clients_attended)
        }
        return statistics
