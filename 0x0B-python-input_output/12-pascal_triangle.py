#!/usr/bin/python3

"""Defines a function for Pascal's Triangle."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for m in range(len(tri) - 1):
            tmp.append(tri[m] + tri[m + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
