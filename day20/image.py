

class Image:
    def __init__(self, algorithm):
        self.image = []
        self.algorithm = [1 if c == "#" else 0 for c in algorithm]
        self.enhance_rounds = 0

    def add_pixel_row(self, line_str):
        self.image.append(
            [0, 0] + [ 1 if c == "#" else 0 for c in line_str] + [0, 0])

    def enhance(self):
        new_image = []
        for y in range(-1, len(self.image) + 1):
            new_row = []
            for x in range(-1, len(self.image[0]) + 1):
                #print("Checking following area:")
                #self.print_area(x, y)
                new_pixel = self.algorithm[self.algorithm_index(x, y)]
                new_row.append(new_pixel)
                #print("new pixel: {}".format(new_pixel))
            #print("got row {} done".format(new_row))
            new_image.append(new_row)
        self.image = new_image
        self.enhance_rounds += 1

    def print_area(self, x, y):
        for yy in range(y-1, y+2):
            for xx in range(x-1, x+2):
                print(self._pixel_at(xx, yy), end="")
            print()

    def algorithm_index(self, x, y):
        numbers = []
        for yy in range(y-1, y+2):
            for xx in range(x-1, x+2):
                numbers.append(self._pixel_at(xx, yy,
                                              default=self.enhance_rounds % 2))
        #print("binary: {}".format("".join([str(n) for n in numbers])))
        #print("base 10: {}".format(int("".join([str(n) for n in numbers]), 2)))
        return int("".join([str(n) for n in numbers]), 2)

    @property
    def lit_pixels(self):
        count = 0
        for row in self.image:
            for pixel in row:
                count += pixel
        return count

    def _pixel_at(self, x, y, default=0):
        if x < 0 or y < 0 or y >= len(self.image) or x >= len(self.image[0]):
            return default
        return self.image[y][x]

    def __str__(self):
        output_chars = []
        for line in self.image:
            output_chars.append(["#" if i else "." for i in line])
        return "\n".join(["".join([c for c in line]) for line in output_chars])

    @property
    def dimensions(self):
        return (len(self.image[0]), len(self.image))
