"""
Advent of code: day XX
"""

import click

from target import Target

def launch_probe(vx, vy, target):
    x = 0
    y = 0
    highest_y = 0
    while not target.overshot(x, y):
        x += vx
        y += vy
        if y > highest_y:
            highest_y = y
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        elif x < target.x_min:
            return -1
        vy -= 1
        if target.hits(x, y):
            return highest_y
    return -1



@click.command()
@click.argument("x_min", type=int)
@click.argument("x_max", type=int)
@click.argument("y_min", type=int)
@click.argument("y_max", type=int)
def solve(x_min, x_max, y_min, y_max):
    """
    Solve the day's exercise.
    """
    target = Target(x_min, x_max, y_min, y_max)
    highest_y = -1
    for vx in range(1, x_max):
        for vy in range(1, 500):
            shot_height = launch_probe(vx, vy, target)
            if shot_height > highest_y:
                highest_y = shot_height
    click.echo("trick shot height: {}".format(highest_y))
    
    hitting_velocities = 0
    for vx in range(1, x_max + 1):
        for vy in range(y_min, 1000):
            if launch_probe(vx, vy, target) > -1:
                hitting_velocities += 1
    click.echo("possible initial velocities: {}".format(hitting_velocities))


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
