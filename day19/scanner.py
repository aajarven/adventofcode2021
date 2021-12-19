
import collections
import copy
from math import pi, sin, cos

import numpy as np

from beacon import Beacon


class Scanner:

    def __init__(self):
        self.coordinates = []
        self.beacons = []

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates
        for beacon in self.beacons:
            beacon.move_origin_to(coordinates)

    def set_orientation(self, rotation_matrix):
        """
        Set the orientations of each beacon measured by this scanner.

        The given x_ax, y_ax and z_ax specify which coordinate corresponds to
        each axis, and whether as negative or positive. E.g. x_ax=1, y_ax=3,
        z_ax=-2 means that x coordinate is the first given coordinate when
        initializing beacons (x1), y is the third (x3) and z is the second, but
        the axis points in the opposite direction.
        """
        for beacon in self.beacons:
            beacon.set_orientation(rotation_matrix)

    def rotate_to_fit(self, known_scanner):
        """
        Find a rotation with which there are at least 12 matching beacons in
        this and the other scanner's range.

        If a suitable rotation is found, it is applied to this scanner and True
        is returned. Otherwise returns False.
        """
        for rotation in self.rotation_matrices():
            rotated_scanner = copy.deepcopy(self)
            rotated_scanner.set_orientation(rotation)
            to_known_scanner = rotated_scanner.vector_to(known_scanner)
            if to_known_scanner is not None:
                self.set_orientation(rotation)
                self.set_coordinates(
                    known_scanner.coordinates - to_known_scanner)
                print("scanner is at \n{}".format(self.coordinates))
                print("rotation for scanner is\n{}".format(rotation))
                return True
        return False

    def vector_to(self, other):
        """
        Return vector from other to self calculated based on 12 overlapping
        beacons.
        """
        diff_vectors = collections.defaultdict(lambda: 0)
        for adjustable_beacon in self.beacons:
            for known_beacon in other.beacons:
                diff = adjustable_beacon.coordinates - known_beacon.coordinates
                diff_vectors[str(diff)] = diff_vectors[str(diff)] + 1
                if diff_vectors[str(diff)] >= 12:
                    return diff
        return None


    def print_beacons(self):
        for beacon in self.beacons:
            print(beacon)

    def rotation_matrices(self):
        """
        Iterate over all possible rotation matrixes in 3D
        """
        for theta_x in [0, pi / 2, pi, 3 * pi / 2]:
            rot_x = np.array([[1, 0, 0],
                              [0, cos(theta_x), -1 * sin(theta_x)],
                              [0, sin(theta_x), cos(theta_x)]
                              ])
            for theta_y in [0, pi / 2, pi, 3 * pi / 2]:
                rot_y = np.array([[cos(theta_y), 0, sin(theta_y)],
                                  [0, 1, 0],
                                  [-1 * sin(theta_y), 0, cos(theta_y)]
                                  ])
                for theta_z in [0, pi / 2, pi, 3 * pi / 2]:
                    rot_z = np.array([[cos(theta_z), -1 * sin(theta_z), 0],
                                      [sin(theta_z), cos(theta_z), 0],
                                      [0, 0, 1]
                                      ])
                    yield np.matmul(np.matmul(rot_x, rot_y), rot_z)

    def add_beacon(self, x1, x2, x3):
        new_beacon = Beacon(x1, x2, x3)
        self.beacons.append(new_beacon)
