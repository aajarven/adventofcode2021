
from digit import ScrambledDigit, Digit


class SegmentDisplay:

    def __init__(self, input_line):
        self.known_segments = {}
        self.digits = []
        for digit_str in input_line.replace("|", "").split():
            self.digits.append(ScrambledDigit(digit_str))

    @property
    def output_digits(self):
        return self.digits[-4:]

    def count_easy(self):
        count = 0
        for digit in self.output_digits:
            if len(digit) in [2, 4, 3, 7]:
                count += 1
        return count

    def output_sum(self):
        self.determine_mapping()
        sum_ = 0
        for digit, exponent in zip(self.output_digits, range(3, -1, -1)):
            unscrambled_digit = Digit(digit, self.known_segments)
            sum_ += unscrambled_digit.value()*(10**exponent)
        return sum_


    def determine_mapping(self):
        all_segments = ScrambledDigit("abcdefg")
        self.known_segments["a"] = (self.seven - self.one).segments
        self.known_segments["c"] = (self.three - self.five).segments
        self.known_segments["f"] = (self.one - ScrambledDigit(self.known_segments["c"])).segments
        self.known_segments["e"] = (all_segments - self.five - self.three).segments
        self.known_segments["b"] = (self.five - self.three).segments
        self.known_segments["d"] = (self.eight - self.zero).segments

    def _print_mapping(self):
        print("{ ", end="")
        for segment in "abcdefg":
            if segment in self.known_segments:
                print("{}: {}, ".format(segment, self.known_segments[segment]),
                        end="")
            else:
                print("{}: -, ".format(segment), end="")
        print("}")

    @property
    def zero(self):
        """
        Return the string corresponding to number 0 (if found)
        """
        if (
                "c" in self.known_segments
                and "e" in self.known_segments):
            for digit in self.digits:
                if (
                        len(digit) == 6
                        and self.known_segments["c"] in digit.segments
                        and self.known_segments["e"] in digit.segments):
                    return digit
        return None

    @property
    def one(self):
        """
        Return the string corresponding to number 1 (if found)
        """
        for digit in self.digits:
            if len(digit) == 2:
                return digit
        return None

    @property
    def two(self):
        if not self.five:
            return None
        for digit in self.digits:
            if len(digit) != 5:
                continue
            if len(digit - self.five) == 2:
                return digit
        return None

    @property
    def three(self):
        if not self.five:
            return None
        for digit in self.digits:
            if len(digit) != 5:
                continue
            if len(digit - self.five) == 1:
                return digit
        return None

    @property
    def four(self):
        for digit in self.digits:
            if len(digit) == 4:
                return digit
        return None

    @property
    def five(self):
        if not self.four and self.one:
            return None

        bd_segments = self.four - self.one
        for digit in self.digits:
            if len(digit) == 5 and not (bd_segments - digit).segments:
                return digit
        return None

    @property
    def six(self):
        if (
                "a" in self.known_segments
                and "b" in self.known_segments
                and "d" in self.known_segments
                and "e" in self.known_segments
                ):
            for digit in self.digits:
                if (
                        len(digit) == 6
                        and self.known_segments["a"] in digit.segments
                        and self.known_segments["b"] in digit.segments
                        and self.known_segments["d"] in digit.segments
                        and self.known_segments["e"] in digit.segments
                        ):
                    return digit

        return None

    @property
    def seven(self):
        for digit in self.digits:
            if len(digit) == 3:
                return digit
        return None

    @property
    def eight(self):
        for digit in self.digits:
            if len(digit) == 7:
                return digit
        return None

    @property
    def nine(self):
        if self.four:
            for digit in self.digits:
                if len(digit) == 6:
                    if len(self.four - digit) == 0:
                        return digit

        return None
