from line import Line


class PriorityLine(Line):

    def generate_current_password(self) -> None:
        self.current_password = f"PR{self.code}"

    def update_line(self) -> None:
        self.increment_line()
        self.generate_current_password()
        self.line.append(self.current_password)
