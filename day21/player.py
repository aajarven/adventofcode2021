from dataclasses import dataclass

class Player:
    """
    A player playing Dirac Dice
    """

    def __init__(self, position, score=0):
        self.position = position
        self.score = score

    def take_turn(self, die):
        for _ in range(3):
            self.move(die.roll())
        self.score += self.position

    def move(self, distance):
        self.position += distance
        while self.position > 10:
            self.position = self.position - 10

    def __eq__(self, other):
        return self.position == other.position and self.score == other.score

    def __str__(self):
        return "Position: {}\tScore: {}".format(self.position, self.score)


@dataclass(frozen=True)
class DiracPlayer:
    position : int
    score : int = 0

    def take_turn(self, distance):
        new_position = self._calculate_position(distance)
        return DiracPlayer(new_position, score=self.score + new_position)

    def _calculate_position(self, after_distance):
        new_position = self.position + after_distance
        while new_position > 10:
            new_position = new_position - 10
        return new_position
