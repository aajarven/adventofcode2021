import collections

class Polymer:

    def __init__(self, template, operations):
        self.operations = {}
        for operation in operations:
            [pair, new_element] = operation.split(" -> ")
            self.operations[pair] = new_element

        self.polymer_letters = {}
        for letter in template:
            self.add_letter(letter)

        self.pairs = {}
        for i in range(len(template) - 1):
            pair = template[i:i+2]
            self.pairs[pair] = self.pairs.get(pair, 0) + 1

    def step(self):
        new_pairs = self.pairs.copy()
        for pair, pair_count in self.pairs.items():
            if pair_count == 0:
                continue
            if pair in self.operations:
                first_letter = pair[0]
                second_letter = self.operations[pair]
                third_letter = pair[1]

                self.add_letter(self.operations[pair], pair_count)

                new_pairs[pair] -= pair_count
                for new_pair in [first_letter+second_letter, second_letter+third_letter]:
                    new_pairs[new_pair] = new_pairs.get(new_pair, 0) + pair_count

        self.pairs = new_pairs

    def add_letter(self, letter, n=1):
        self.polymer_letters[letter] = self.polymer_letters.get(letter, 0) + n

    def most_common_letter_count(self):
        return max(self.polymer_letters.values())

    def least_common_letter_count(self):
        return min(self.polymer_letters.values())

    def __str__(self):
        return str(self.polymer_letters)
