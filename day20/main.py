"""
Advent of code: day XX
"""

import click

from image import Image


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the day's exercise.
    """
    input_data = [line for line in input_file.readlines()]

    algorithm = input_data[0].strip()

    image = Image(algorithm)
    for line in input_data[2:]:
        image.add_pixel_row(line.strip())

    image.enhance()
    image.enhance()
    click.echo("lit after two rounds: {}".format(image.lit_pixels))
    for i in range(48):
        image.enhance()
    click.echo("lit after 50 rounds: {}".format(image.lit_pixels))

if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
