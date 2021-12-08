

class ScrambledDigit:

    def __init__(self, segment_str):
        segments = [c for c in segment_str]
        segments.sort()
        self.segment_str = "".join(segments)

    @property
    def segments(self):
        return self.segment_str

    def __sub__(self, other):
        result = ""
        for letter in self.segment_str:
            if letter not in other.segments:
                result += letter
        return ScrambledDigit(result)

    def __len__(self):
        return len(self.segment_str)

    def __eq__(self, other):
        return self.segments == other.segments

    def __str__(self):
        return self.segments


class Digit:
    def __init__(self, scrambled_digit, digit_mapping):
        """
        Unscrambled digit.

        NB: We don't care about the segment g, as it is not needed to identify
        any number.
        """
        self.segments = {
            "a": False,
            "b": False,
            "c": False,
            "d": False,
            "e": False,
            "f": False,
            }
        for correct_segment, scrambled_segment in digit_mapping.items():
            if scrambled_segment in scrambled_digit.segments:
                self.segments[correct_segment] = True

    def value(self):
        if (
                self.segments["a"]
                and self.segments["b"]
                and self.segments["c"]
                and not self.segments["d"]
                and self.segments["e"]
                and self.segments["f"]
                ):
            return 0
        elif (
                not self.segments["a"]
                and not self.segments["b"]
                and self.segments["c"]
                and not self.segments["d"]
                and not self.segments["e"]
                and self.segments["f"]
                ):
            return 1
        elif (
                self.segments["a"]
                and not self.segments["b"]
                and self.segments["c"]
                and self.segments["d"]
                and self.segments["e"]
                and not self.segments["f"]
                ):
            return 2
        elif (
                self.segments["a"]
                and not self.segments["b"]
                and self.segments["c"]
                and self.segments["d"]
                and not self.segments["e"]
                and self.segments["f"]
                ):
            return 3
        elif (
                not self.segments["a"]
                and self.segments["b"]
                and self.segments["c"]
                and self.segments["d"]
                and not self.segments["e"]
                and self.segments["f"]
                ):
            return 4
        elif (
                self.segments["a"]
                and self.segments["b"]
                and not self.segments["c"]
                and self.segments["d"]
                and not self.segments["e"]
                and self.segments["f"]
                ):
            return 5
        elif (
                self.segments["a"]
                and self.segments["b"]
                and not self.segments["c"]
                and self.segments["d"]
                and self.segments["e"]
                and self.segments["f"]
                ):
            return 6
        elif (
                self.segments["a"]
                and not self.segments["b"]
                and self.segments["c"]
                and not self.segments["d"]
                and not self.segments["e"]
                and self.segments["f"]
                ):
            return 7
        elif (
                self.segments["a"]
                and self.segments["b"]
                and self.segments["c"]
                and self.segments["d"]
                and self.segments["e"]
                and self.segments["f"]
                ):
            return 8
        elif (
                self.segments["a"]
                and self.segments["b"]
                and self.segments["c"]
                and self.segments["d"]
                and not self.segments["e"]
                and self.segments["f"]
                ):
            return 9
