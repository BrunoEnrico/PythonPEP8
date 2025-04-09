from normal_line import NormalLine
from priority_line import PriorityLine

from constants import NORMAL_LINE_FACTORY, PRIORITY_LINE_FACTORY


class LineFactory:

    @staticmethod
    def get_line_factory(line: str) -> NormalLine | PriorityLine:
        if line == NORMAL_LINE_FACTORY:
            return NormalLine()
        if line == PRIORITY_LINE_FACTORY:
            return PriorityLine()

        raise NotImplementedError("Class don't exist!")
