from line_factory import LineFactory
from detailed_statistics import DetailedStatistics
from resumed_statistics import ResumedStatistics


class Main:

    @staticmethod
    def process() -> None:
        line = LineFactory.get_line_factory("normal")
        line.update_line()
        line.update_line()
        print(line.call_client(10))
        print(line.statistics(DetailedStatistics("10", 10)))
        print(line.statistics(ResumedStatistics("10", 10)))


if __name__ == '__main__':
    main = Main()
    main.process()
