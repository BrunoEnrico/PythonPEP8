class PrioritaryLine:
    code: int = 0
    line: list = []
    clients_attended: list = []
    current_password: str = ""

    def generate_current_password(self) -> None:
        self.current_password = f"PR{self.code}"

    def increment_line(self) -> None:
        if self.code > 100:
            self.code = 0
        else:
            self.code += 1

    def update_line(self) -> None:
        self.increment_line()
        self.generate_current_password()
        self.line.append(self.current_password)

    def call_client(self, desk_number: int) -> str:
        current_client = self.line.pop(0)
        self.clients_attended.append(current_client)
        return f"{current_client} on {desk_number}"

    def statistics(self, day: str, agency: int, flag: str) -> dict:
        statistics = {}
        if flag != "detail":
            statistics = {f"{agency} -- {day}": len(self.clients_attended)}
        else:
            statistics["day"] = day
            statistics["agency"] = agency
            statistics["clients_attended"] = self.clients_attended
            statistics["amount_clients_attended"] = len(self.clients_attended)

        return statistics