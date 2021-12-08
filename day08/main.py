"""
Advent of code: day XX
"""

import click

from segment_display import SegmentDisplay


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the day's exercise.
    """
    easy_count = 0
    difficult_sum = 0
    for line in input_file:
        sd = SegmentDisplay(line)
        easy_count += sd.count_easy()
        difficult_sum += sd.output_sum()
    click.echo("Number of easy digits: {}".format(easy_count))
    click.echo("Sum of outputs: {}".format(difficult_sum))


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
