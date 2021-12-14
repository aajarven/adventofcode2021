"""
Advent of code: day 14
"""

import click

from polymer import Polymer

@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the day's exercise.
    """
    initial_polymer = input_file.readline().strip()

    operations = []
    for line in input_file.readlines():
        if not line.strip():
            continue
        operations.append(line.strip())

    polymer = Polymer(initial_polymer, operations)
    for _ in range(10):
        polymer.step()
    click.echo("Result after 10 steps: {}"
               "".format(polymer.most_common_letter_count()
                         - polymer.least_common_letter_count()))

    for _ in range(30):
        polymer.step()
    click.echo("Result after 40 steps: {}"
               "".format(polymer.most_common_letter_count()
                         - polymer.least_common_letter_count()))

if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
