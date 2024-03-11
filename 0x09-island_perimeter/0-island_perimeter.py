#!/usr/bin/python3
"""
module for island_perimeter
"""


def island_perimeter(grid):
    """ returns the perimeter of the island described in grid
    """
    lands, joint = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                lands += 1
            if j != 0 and grid[i][j] == 1 and grid[i][j-1] == 1:
                joint += 1
            if i != 0 and grid[i][j] == 1 and grid[i-1][j] == 1:
                joint += 1
    return (lands * 4) - (joint * 2)
