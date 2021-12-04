"""
Advent of code: Bingo
"""

import click

from reader import read_bingo


@click.command()
@click.argument("input_file", type=click.File("r"))
def bingo(input_file):
    """
    Solve the bingo problem
    """
    print("Part 1: first winning board")
    game = read_bingo(input_file)
    first_winner = game.play_to_first()
    click.echo(first_winner)
    click.echo("board score: {}".format(first_winner.score))
    click.echo("latest number: {}".format(game.latest_draw))
    click.echo("total score: {}"
               "".format(first_winner.score * game.latest_draw))

    last_winner = game.continue_to_last()
    click.echo(last_winner)
    click.echo("board score: {}".format(last_winner.score))
    click.echo("latest number: {}".format(game.latest_draw))
    click.echo("total score: {}"
               "".format(last_winner.score * game.latest_draw))


if __name__ == "__main__":
    bingo()  # pylint: disable=no-value-for-parameter
