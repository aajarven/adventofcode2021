"""
Class for representing a game of bingo.
"""

class Bingo:
    """
    A game of bingo
    """

    def __init__(self, draws=None):
        self.boards = []
        if draws:
            self.draws = draws
        else:
            self.draws = []

        self.winning_board = None
        self.draw_count = 0

    @property
    def latest_draw(self):
        """
        Return the last drawn number
        """
        return self.draws[self.draw_count - 1]

    def add_board(self, board):
        """
        Add a new BingoBoard to the game.
        """
        self.boards.append(board)

    def play_to_first(self):
        """
        Play the game until there is a winning board

        :returns: the winning board
        """
        for number in self.draws:
            self.draw_count += 1
            for board in self.boards:
                board.mark(number)
                if board.bingo():
                    return board
        raise ValueError("No winning board found")

    def continue_to_last(self):
        """
        Play the game until all boards have won
        """
        latest_bingoer = None
        for number in self.draws[self.draw_count:]:
            if all([board.bingo() for board in self.boards]):
                return latest_bingoer
            self.draw_count += 1
            for board in self.boards:
                if board.bingo():
                    continue
                else:
                    board.mark(number)
                    if board.bingo():
                        latest_bingoer = board
