"""
A single board for a game of bingo
"""

class BingoBoard:
    """
    A 5*5 bingo board
    """

    def __init__(self, numbers):
        """
        Create a new board.

        :nubmers: A 5*5 array of integers representing the board
        """
        self.numbers = numbers
        self.marked = [[False for _ in range(5)] for _ in range(5)]

    def mark(self, number):
        """
        Mark a new number on the board.

        If the number is not present, nothing happens.
        """
        for i in range(5):
            for j in range(5):
                if self.numbers[i][j] == number:
                    self.marked[i][j] = True

    def bingo(self):
        """
        Return True if there is a bingo on this board.
        """
        # check rows
        for row in self.marked:
            if all(row):
                return True

        # check columns
        for column in range(len(self.marked)):
            if all([row[column] for row in self.marked]):
                return True

        return False


    @property
    def score(self):
        """
        Return the sum of all unmarked numbers on the board
        """
        score = 0
        for row in range(len(self.numbers)):
            for column in range(len(self.numbers[row])):
                if not self.marked[row][column]:
                    score += self.numbers[row][column]
        return score

    def __str__(self):
        horizontal_border = "+" + "-"*14 + "+"

        board_str = "{0} {0}\n".format(horizontal_border)

        for i in range(len(self.numbers)):
            board_str += "|{:>2} {:>2} {:>2} {:>2} {:>2}| ".format(*self.numbers[i])
            board_str += "|{:>2} {:>2} {:>2} {:>2} {:>2}|\n".format(
                *["X" if marked else " " for marked in self.marked[i]]
                )
        board_str += "{0} {0}".format(horizontal_border)
        return board_str
