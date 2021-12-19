import numpy as np


class Beacon:

    def __init__(self, x1, x2, x3):
        """
        Create a new beacon with unknown orientation
        """
        self.original_coordinates = np.array([[x1], [x2], [x3]])
        self.coordinates = self.original_coordinates

    def set_orientation(self, rotation_matrix):
        """
        Set the orientation of the coordinate system used.

        The given x_ax, y_ax and z_ax specify which coordinate corresponds to
        each axis, and whether as negative or positive. E.g. x_ax=1, y_ax=3,
        z_ax=-2 means that x coordinate is the first given coordinate when
        initializing this beacon (x1), y is the third (x3) and z is the second,
        but the axis points in the opposite direction.
        """
        self.coordinates = self.rotated_coordinates(rotation_matrix)

    def offset(self, beacon):
        return self.coordinates - beacon.coordinates

    def move_origin_to(self, coordinates):
        """
        Change the coordinates of this beacon to be relative to given
        coordinates.
        """
        self.coordinates = self.coordinates + coordinates

    def relative_coordinates(self, coordinates):
        """
        Return the coordinates of this beacon as seen from given coordinates.
        """
        return self.coordinates + coordinates

    def rotated_coordinates(self, rotation_matrix):
        return np.matmul(rotation_matrix,
                         self.original_coordinates)

    def __str__(self):
        return "[{:>6}{:>6}{:>6} ]".format(
            *[round(coord) for coord in np.transpose(self.coordinates)[0]])

    def __eq__(self, other):
        return np.allclose(self.coordinates, other.coordinates)

    def __hash__(self):
        return hash(str(self))


def _sign(x):
    return x / abs(x)
