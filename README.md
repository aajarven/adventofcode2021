# Advent of Code 2021

My advent of code solutions. Practicing some good old-fashioned C here and doing
an occasional python solution.

## Templates

The [c-template](c-template) directory contains a starting point for working on the
individual exercises. The makefile within has targets `run` for running the
program (using default input from `data/input.txt`), `example` for running
using input from (`data/example.txt`) and `valgrind` for checking for memory
leaks using the same input file.

Similarly, a [python-template](python-template) exists to act as a starting point
for python solutions.

## Utils

Some generic functions, e.g. ones for reading the input from a file, can be
found in [utils](utils).
