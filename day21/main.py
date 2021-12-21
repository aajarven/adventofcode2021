"""
Advent of code: day 21
"""

import collections
from functools import cache
import itertools

import click

from die import Die
from player import Player, DiracPlayer


@click.command()
@click.argument("player1_start", type=int)
@click.argument("player2_start", type=int)
def solve(player1_start, player2_start):
    """
    Solve the day's exercise.
    """
    die = Die()
    p1 = Player(player1_start)
    p2 = Player(player2_start)
    winner = None
    loser = None

    while True:
        p1.take_turn(die)
        if p1.score >= 1000:
            winner = p1
            loser = p2
            break
        p2.take_turn(die)
        if p2.score >= 1000:
            winner = p2
            loser = p1
            break

    click.echo("{} rolls".format(die.roll_count))
    click.echo("The loser has {} points".format(loser.score))
    click.echo("Product: {}".format(die.roll_count * loser.score))

    p1 = DiracPlayer(player1_start)
    p2 = DiracPlayer(player2_start)
    result = count_wins(p1, p2, 1)
    click.echo(max(result))

@cache
def count_wins(player1, player2, current_player):
    if player1.score >= 21:
        return [1, 0]
    elif player2.score >= 21:
        return [0, 1]

    wins = [0, 0]

    roll_frequencies = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1,
    }
    
    for roll in roll_frequencies:

        if current_player == 1:
            current_player_after_turn = player1.take_turn(roll)
            new_wins = count_wins(current_player_after_turn, player2, 2)
        else:
            current_player_after_turn = player2.take_turn(roll)
            new_wins = count_wins(player1, current_player_after_turn, 1)
        
        wins[0] += new_wins[0] * roll_frequencies[roll]
        wins[1] += new_wins[1] * roll_frequencies[roll]

    return wins


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter

