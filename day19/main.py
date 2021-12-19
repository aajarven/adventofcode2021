"""
Advent of code: day 19
"""

import queue

import click
import numpy as np

from scanner import Scanner


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the day's exercise.
    """
    scanners = []
    scanner_oriented = []
    for line in input_file:
        if line.startswith("---"):
            scanners.append(Scanner())
            scanner_oriented.append(False)
        elif not line.strip():
            continue
        else:
            coordinates = [int(coordinate) for coordinate in
                           line.strip().split(",")]
            scanners[-1].add_beacon(*coordinates)

    scanners[0].set_orientation(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
    scanners[0].set_coordinates(np.array([[0], [0], [0]]))
    scanner_oriented[0] = True

    newly_oriented_scanners = queue.Queue()
    newly_oriented_scanners.put(scanners[0])

    while not newly_oriented_scanners.empty():
        newly_oriented_scanner = newly_oriented_scanners.get()
        print("orienting other scanners relative to the scanner at\n{}"
              "".format(newly_oriented_scanner.coordinates))
        for i in range(len(scanners)):
            if not scanner_oriented[i]:
                print("trying to orient scanner {}".format(i))
                if scanners[i].rotate_to_fit(newly_oriented_scanner):
                    newly_oriented_scanners.put(scanners[i])
                    scanner_oriented[i] = True
                    print("oriented scanner {}".format(i))
                    for beacon in scanners[i].beacons:
                        print(beacon)

    beacons = set()
    for scanner in scanners:
        for beacon in scanner.beacons:
            beacons.add(beacon)
    click.echo("There are {} distinct beacons".format(len(beacons)))

if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
