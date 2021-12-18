"""
Advent of code: day 18
"""

import copy

import click

from snailfish_numbers import SNumber


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the day's exercise.
    """
    numbers = []
    for line in input_file:
        numbers.append(SNumber.from_string(line))

    snailsum = numbers[0]
    for number in numbers[1:]:
        snailsum = snailsum + number
        while snailsum.reduce():
            pass

    click.echo("magnitude of the total sum: {}".format(snailsum.magnitude))

    numbers = []
    input_file.seek(0)
    for line in input_file:
        numbers.append(SNumber.from_string(line))

    max_magnitude = 0
    for number1 in numbers:
        for number2 in numbers:
            if number1 == number2:
                continue
            pairsum = copy.deepcopy(number1) + copy.deepcopy(number2)
            while pairsum.reduce():
                pass
            mag = pairsum.magnitude
            if mag > max_magnitude:
                max_magnitude = mag
    click.echo("max magnitude of a single sum: {}".format(max_magnitude))


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
