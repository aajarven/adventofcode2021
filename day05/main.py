"""
Advent of code: day 05
"""

import click

from ocean_floor import OceanFloor
from vent_line import SimpleVentLine, ComplexVentLine


@click.command()
@click.argument("input_file", type=click.File("r"))
@click.argument("size", type=int)
def solve(input_file, size):
    """
    Solve the day's exercise.
    """
    simple_ocean_floor = create_simple_ocean_floor(input_file, size)
    click.echo("Horizontal and vertical intersects: {}"
               "".format(simple_ocean_floor.count_intersects()))
    complex_ocean_floor = create_complex_ocean_floor(input_file, size)
    click.echo("Horizontal, vertical and diagonal intersects: {}"
               "".format(complex_ocean_floor.count_intersects()))
    # click.echo(complex_ocean_floor)


def create_simple_ocean_floor(input_file, size=1000):
    """
    Read all vent lines from given file, add them to an ocean floor, and
    return that.

    Only horizontal and vertical vent lines are included.
    """
    ocean_floor = OceanFloor(size)
    input_file.seek(0)

    for line in input_file.readlines():
        ocean_floor.add_vents(SimpleVentLine(line))

    return ocean_floor


def create_complex_ocean_floor(input_file, size=1000):
    """
    Read all vent lines from given file and return an ocean floor with them.

    Diagonal vent lines are also allowed.
    """
    ocean_floor = OceanFloor(size)
    input_file.seek(0)

    for line in input_file.readlines():
        ocean_floor.add_vents(ComplexVentLine(line))

    return ocean_floor


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
