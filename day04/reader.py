"""
Input handling scripts
"""

from bingo import Bingo
from bingoboard import BingoBoard


def read_bingo(input_file):
    """
    Read a game of bingo from an input file.
    """
    lines = input_file.readlines()

    draws = [int(number) for number in lines[0].split(",")]

    bingogame = Bingo(draws)

    board_numbers = []
    for line in lines[1:]:
        if not line.strip():
            continue
        else:
            board_numbers.append([int(number) for number in line.split()])
        if len(board_numbers) == 5:
            bingogame.add_board(BingoBoard(board_numbers))
            board_numbers = []

    return bingogame
