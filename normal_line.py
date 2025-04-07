from line import Line


class NormalLine(Line):

    def generate_current_password(self) -> None:
        self.current_password = f"NM{self.code}"

    def update_line(self) -> None:
        self.increment_line()
        self.generate_current_password()
        self.line.append(self.current_password)
