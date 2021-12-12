"""
Advent of code: day XX
"""

import click

from cave import CaveSystem


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the day's exercise.
    """

    cave_system = CaveSystem()
    for line in input_file:
        cave_system.add_from_input(line)

    click.echo("Routes: {}"
               "".format(cave_system.dfs_count(cave_system.get("start"))))
    click.echo("Routes with two visits: {}"
               "".format(
                   cave_system.dfs_count(cave_system.get("start"),
                                         True)))


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
