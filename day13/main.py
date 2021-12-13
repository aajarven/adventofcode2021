"""
Advent of code: day XX
"""

import click

from paper import Paper


@click.command()
@click.argument("input_file", type=click.File("r"))
#@click.argument("page_width", type=int)
#@click.argument("page_height", type=int)
def solve(input_file):
    """
    Solve the day's exercise.
    """
    manual_page = Paper()

    for line in input_file:
        if not line.strip():
            break
        manual_page.mark_dot_from_input(line)

    for line in input_file:
        spec = line.strip("fold along").strip()
        coordinate = int(spec.split("=")[1])
        if "x" in spec:
            manual_page.fold(x=coordinate)
        elif "y" in spec:
            manual_page.fold(y=coordinate)
        click.echo("There are now {} dots visible"
                   "".format(manual_page.n_dots()))

    manual_page.print_page()


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
