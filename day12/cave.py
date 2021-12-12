

class Cave:
    """
    A single cave in the system.

    Knows its name, neighbors, and how many times it has been visited.
    """

    def __init__(self, name, neighbors=None):
        self.name = name
        self.visited = 0
        if neighbors:
            self.neighbors = neighbors
        else:
            self.neighbors = []

    @property
    def is_big(self):
        """
        Return True if this is a big cave, otherwise False.
        """
        return self.name.isupper()

    @property
    def is_small(self):
        """
        Return True if this is a small cave, otherwise False.
        """
        return self.name.islower()

    @property
    def is_end(self):
        """
        Return True if this is the end cave, otherwise False.
        """
        return self.name == "end"

    @property
    def is_start(self):
        """
        Return True if this is the start cave, otherwise False.
        """
        return self.name == "start"


class CaveSystem:
    """
    A cave system consisting of multiple caves.
    """

    def __init__(self):
        self.caves = []

    def add_from_input(self, input_line):
        """
        Add a new line based on a string in format "{start_name}-{end_name}".
        """
        [start, end] = input_line.strip().split("-")
        start_cave = self.get(start)
        end_cave = self.get(end)
        start_cave.neighbors.append(end_cave)
        end_cave.neighbors.append(start_cave)

    def get(self, cave_name):
        """
        Return a cave by that name if present in system, otherwise a new cave.
        """
        for cave in self.caves:
            if cave.name == cave_name:
                return cave

        new_cave = Cave(cave_name)
        self.caves.append(new_cave)
        return new_cave

    def dfs_count(self, current_node, allow_visit_twice=False):
        """
        Do a depth first search of the cave system and return the number of
        routes from current node to the end cave.

        If `allow_visit_twice` is set to True, a single small cave can be
        visited twice instead of just once.
        """
        if current_node.is_end:
            return 1
        if current_node.visited and current_node.is_small:
            if allow_visit_twice and not current_node.is_start:
                return self._visit_neighbors(current_node, False)
            return 0

        count = self._visit_neighbors(current_node, allow_visit_twice)
        return count

    def _visit_neighbors(self, node, allow_visit_twice):
        """
        Do a dfs_count starting from this node.
        """
        found_routes = 0
        node.visited += 1
        for neighbor in node.neighbors:
            found_routes += self.dfs_count(neighbor, allow_visit_twice)
        node.visited -= 1
        return found_routes
