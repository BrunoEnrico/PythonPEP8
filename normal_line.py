from line import Line
from constants import NORMAL_CODE


class NormalLine(Line):

    def generate_current_password(self) -> None:
        self.current_password = f"${NORMAL_CODE}{self.code}"
