from normal_line import NormalLine
from prioritary_line import PrioritaryLine


class Main:
    def __init__(self):
        self.line = NormalLine()
        self.priority_line = PrioritaryLine()

    def process(self):
        # self.line.update_line()
        # self.line.update_line()
        # self.line.update_line()
        # self.line.update_line()
        # print(self.line.call_client("12"))
        self.priority_line.update_line()
        self.priority_line.update_line()
        self.priority_line.update_line()
        self.priority_line.update_line()
        self.priority_line.call_client(1)
        self.priority_line.call_client(2)
        print(self.priority_line.statistics("05", 41, "detail"))


if __name__ == '__main__':
    main = Main()
    main.process()
