"""
Representation for one line of hydrothermal vents
"""


class SimpleVentLine:
    """
    A horizontal or vertical line of hydrothermal vents
    """

    def __init__(self, input_line):
        """
        Create a new line of hydrothermal vents

        :input_line: A definition of the vent line from puzzle input. e.g.
                     "0,9 -> 5,9"
        """
        (start, end) = input_line.split(" -> ")
        self.start_x = int(start.split(",")[0])
        self.start_y = int(start.split(",")[1])
        self.end_x = int(end.split(",")[0])
        self.end_y = int(end.split(",")[1])

    def loop_x(self):
        """
        Yield all x coordinates in horizontal line represented by this VentLine
        """
        # pylint: disable=invalid-name
        if self.start_x < self.end_x:
            for x in range(self.start_x, self.end_x + 1):
                yield x
        else:
            for x in range(self.start_x, self.end_x - 1, -1):
                yield x

    def loop_y(self):
        """
        Yield all y coordinates in vertical line represented by this VentLine
        """
        # pylint: disable=invalid-name
        if self.start_y < self.end_y:
            for y in range(self.start_y, self.end_y + 1):
                yield y
        else:
            for y in range(self.start_y, self.end_y - 1, -1):
                yield y

    def vents(self):
        """
        Return a list of all coordinates with a vent in this line.
        """
        # pylint: disable=invalid-name
        if self.start_x == self.end_x:
            for y in self.loop_y():
                yield [self.start_x, y]
        elif self.start_y == self.end_y:
            for x in self.loop_x():
                yield [x, self.start_y]


class ComplexVentLine(SimpleVentLine):
    """
    Represent a vent line that can be horizontal, vertical or diagonal.
    """
    # pylint: disable=invalid-name
    def vents(self):
        simple_vents = list(super().vents())
        if simple_vents:
            for vent in simple_vents:
                yield vent
        elif (self.start_x != self.end_x
                and
                self.start_y != self.end_y):
            for x, y in zip(self.loop_x(), self.loop_y()):
                yield [x, y]
