#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    m = []
    if n <= 0:
        return m
    m = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(m[i - 1]) - 1):
            curr = m[i - 1]
            temp.append(m[i - 1][j] + m[i - 1][j + 1])
        temp.append(1)
        m.append(temp)
    return m
