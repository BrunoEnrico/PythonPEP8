from line import Line
from constants import PRIORITARY_CODE


class PriorityLine(Line):

    def generate_current_password(self) -> None:
        self.current_password = f"${PRIORITARY_CODE}{self.code}"
