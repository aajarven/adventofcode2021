"""
Ocean floor class
"""


class OceanFloor:
    """
    Store information about all the hydrothermal vents
    """

    def __init__(self, size=1000):
        """
        Create a new ocean floor.

        :size: Set the dimensions of the ocean floor to size*size
        """
        self.vent_counts = [[0 for _ in range(size)] for _ in range(size)]

    def add_vents(self, vent_line):
        """
        Increment vent counts according to the given VentLine
        """
        # pylint: disable=invalid-name
        for (x, y) in vent_line.vents():
            self.vent_counts[x][y] += 1

    def count_intersects(self):
        """
        Return the number of points at which at least two lines overlap
        """
        intersects = 0
        for row in self.vent_counts:
            for count in row:
                if count >= 2:
                    intersects += 1
        return intersects

    def __str__(self):
        # pylint: disable=invalid-name
        ocean_str = ""
        for x in range(len(self.vent_counts)):
            for y in range(len(self.vent_counts)):
                ocean_str += str(self.vent_counts[y][x])
            ocean_str += "\n"
        return ocean_str
