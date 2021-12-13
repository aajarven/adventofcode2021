

class Paper:

    def __init__(self):
        self.dots = []

    def mark_dot_from_input(self, line):
        coordinates = [int(coordinate) for coordinate in line.strip().split(",")]
        self.dots.append(coordinates)

    def print_dots(self):
        for coordinates in self.dots:
            print(coordinates)

    def fold(self, x=None, y=None):
        if x:
            for dot in self.dots:
                if dot[0] > x:
                    dot[0] = x - ( dot[0] - x )
        elif y:
            for dot in self.dots:
                if dot[1] > y:
                    dot[1] = y - ( dot[1] - y )

        self.remove_duplicates()

    def remove_duplicates(self):
        unique_dots = []
        for dot in self.dots:
            if dot not in unique_dots:
                unique_dots.append(dot)
        self.dots = unique_dots

    def n_dots(self):
        return len(self.dots)

    def paper_width(self):
        width = 0
        for dot in self.dots:
            if dot[0] > width:
                width = dot[0]
        return width + 1

    def paper_height(self):
        height = 0
        for dot in self.dots:
            if dot[1] > height:
                height = dot[1]
        return height + 1

    def print_page(self):
        print_array = [
                ["." for _ in range(self.paper_width())]
                for _ in range(self.paper_height())]

        for dot in self.dots:
            print_array[dot[1]][dot[0]] = "#"
        
        for line in print_array:
            print("".join(line))
        print()
