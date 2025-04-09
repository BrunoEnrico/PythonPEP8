from line_factory import LineFactory


class Main:

    @staticmethod
    def process() -> None:
        line = LineFactory.get_line_factory("normal")
        print(line)


if __name__ == '__main__':
    main = Main()
    main.process()
