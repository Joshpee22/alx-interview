#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""

import sys

def generate_solutions(row, column):
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution

def place_queen(queen, column, prev_solution):
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [(queen, x)])
    return safe_position

def is_safe(q, x, array):
    return x not in (col for (_, col) in array) and all(abs(col - x) != q - i for i, (row, col) in enumerate(array))

def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def print_solution(array):
    for q, x in array:
        line = "." * x + "Q" + "." * (len(array) - x - 1)
        print(line)
    print()

def print_solutions(solutions):
    for array in solutions:
        print_solution(array)

def n_queens():
    n = init()
    solutions = generate_solutions(n, n)
    print_solutions(solutions)

if __name__ == '__main__':
    n_queens()

