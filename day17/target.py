

class Target:

    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def hits(self, x, y):
        return (
                x >= self.x_min and
                x <= self.x_max and
                y >= self.y_min and
                y <= self.y_max
                )

    def overshot(self, x, y):
        return y < self.y_min or x > self.x_max
