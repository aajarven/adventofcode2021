

class Die:
    """
    A deterministic die that rolls numbers 1, 2, ..., 99, 100, 1, 2, ...
    """

    def __init__(self):
        self._next_roll = 1
        self.roll_count = 0

    def roll(self):
        self.roll_count += 1
        roll = self._next_roll
        self._next_roll += 1
        if self._next_roll > 100:
            self._next_roll = 1
        return roll
