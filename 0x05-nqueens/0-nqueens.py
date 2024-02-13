#!/usr/bin/python3
"""N Queen Problem Solution With Backtracking"""
from sys import argv


def errorHandler(msg):
    """Print error message and exit with status 1"""
    print(msg)
    exit(1)


if len(argv) != 2:
    errorHandler("Usage: nqueens N")

try:
    n = int(argv[1])
except ValueError:
    errorHandler("N must be a number")

if n < 4:
    errorHandler("N must be at least 4")


class Nqueens():
    """Nqueens solution"""

    def __init__(self, n):
        self.n = n
        self.col = set()
        self.rdig = set()
        self.ldig = set()

        self.solutions = []
        self.board = [[0] * n for i in range(n)]

        # start backtracking
        self.backtrack(0)
        # print solutions
        for solution in self.solutions:
            print(solution)

    def backtrack(self, r):
        if r >= self.n:
            solution = []
            for row in range(len(self.board)):
                for col in range(len(self.board[row])):
                    self.board[row][col] and solution.append([row, col])
            self.solutions.append(solution)

        for c in range(self.n):
            if c in self.col or (r + c) in self.rdig or (r - c) in self.ldig:
                continue

            self.col.add(c)
            self.ldig.add(r - c)
            self.rdig.add(r + c)
            self.board[r][c] = 1

            self.backtrack(r+1)

            self.col.remove(c)
            self.ldig.remove(r - c)
            self.rdig.remove(r + c)
            self.board[r][c] = 0


Nqueens(n)
