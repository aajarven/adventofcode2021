"""
Advent of code: day 16
"""

import click
from bits import Packet, BitStream

def _hex_to_bin(input_str):
    return bin(int(input_str, 16))[2:]



@click.command()
@click.argument("input_file", type=click.File("r"))
@click.option("--binary_input/--hex-input", "-b/-h", default=False)
def solve(input_file, binary_input):
    """
    Solve the day's exercise.
    """
    data_str = input_file.readline()
    if not binary_input:
        data_str = _hex_to_bin(data_str)

    p = Packet.parse(BitStream(data_str))
    click.echo("Version sum: {}".format(p.version_sum()))
    click.echo("Total value: {}".format(p.value))


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
