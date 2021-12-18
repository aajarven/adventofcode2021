import math


class SNumber:
    def __init__(self, left, right, parent):
        self.left = left
        self.right = right
        self.parent = parent
        for child in [self.left, self.right]:
            if isinstance(child, SNumber):
                child.parent = self

    @classmethod
    def from_string(cls, string):
        result = None
        stack = []
        for c in string:  # pylint: disable=invalid-name
            if c.isdigit():
                stack.append(int(c))
            elif c == "]":
                right = stack.pop()
                left = stack.pop()
                result = SNumber(left, right, None)
                stack.append(result)
        return result

    def __add__(self, other):
        result = SNumber(left=self, right=other, parent=None)
        self.parent = result
        other.parent = result
        return result

    @property
    def magnitude(self):
        if isinstance(self.left, SNumber):
            m_left = 3*self.left.magnitude
        else:
            m_left = 3*self.left
        if isinstance(self.right, SNumber):
            m_right = 2*self.right.magnitude
        else:
            m_right = 2*self.right
        return m_left + m_right

    @property
    def depth(self):
        if not self.parent:
            return 0
        return self.parent.depth + 1

    def __str__(self):
        left = str(self.left)
        right = str(self.right)
        return "[{}, {}]".format(left, right)

    @property
    def is_leaf(self):
        return isinstance(self.left, int) and isinstance(self.right, int)

    @property
    def leftmost_leaf(self):
        if self.is_leaf:
            return self
        if not isinstance(self.left, SNumber):
            return self
        return self.left.leftmost_leaf

    @property
    def rightmost_leaf(self):
        if self.is_leaf:
            return self
        if not isinstance(self.right, SNumber):
            return self
        return self.right.rightmost_leaf

    @property
    def left_neighbour(self):
        if not self.parent:
            return None
        if self.parent.left == self:
            return self.parent.left_neighbour
        elif not isinstance(self.parent.left, SNumber):
            return self.parent
        return self.parent.left.rightmost_leaf

    @property
    def right_neighbour(self):
        if not self.parent:
            return None
        if self.parent.right == self:
            return self.parent.right_neighbour
        elif not isinstance(self.parent.right, SNumber):
            return self.parent
        return self.parent.right.leftmost_leaf

    def reduce(self):
        if self.explode():
            return True
        if self.split():
            return True
        return False

    def explode(self):
        if self.is_leaf and self.depth >= 4:
            left_neighbour = self.left_neighbour
            if left_neighbour:
                if isinstance(left_neighbour.right, SNumber):
                    left_neighbour.left += self.left
                else:
                    left_neighbour.right += self.left
            right_neighbour = self.right_neighbour
            if right_neighbour:
                if isinstance(right_neighbour.left, SNumber):
                    right_neighbour.right += self.right
                else:
                    right_neighbour.left += self.right

            if self == self.parent.left:
                self.parent.left = 0
            else:
                self.parent.right = 0
            return True
        else:
            exploded = False
            if isinstance(self.left, SNumber):
                exploded = self.left.explode()
            if not exploded and isinstance(self.right, SNumber):
                exploded = self.right.explode()
            return exploded

    def split(self):
        split = False
        if isinstance(self.left, SNumber):
            split = self.left.split()
        elif self.left >= 10:
            new_number = SNumber(math.floor(self.left/2.0),
                                 math.ceil(self.left/2.0),
                                 self)
            self.left = new_number
            return True
        if not split:
            if isinstance(self.right, SNumber):
                split = self.right.split()
            elif self.right >= 10:
                new_number = SNumber(math.floor(self.right/2.0),
                                     math.ceil(self.right/2.0),
                                     self)
                self.right = new_number
                return True
        return split
