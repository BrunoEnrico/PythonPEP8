from normal_line import NormalLine

class Main:
    def __init__(self):
        self.line = NormalLine()

    def process(self):
        self.line.update_line()
        self.line.update_line()
        self.line.update_line()
        self.line.update_line()
        print(self.line.call_client("12"))




if __name__ == '__main__':
    main = Main()
    main.process()