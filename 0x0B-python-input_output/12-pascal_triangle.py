#!/usr/bin/python3
"""Writes a pascal triangle"""


def pascal_triangle(n):
    """Pascal triangle

    Returns a lists of inteers representing the triangle
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trian = triangles[-1]
        temp = [1]
        for twe in range(len(trian) - 1):
            temp.append(trian[twe] + trian[twe + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
