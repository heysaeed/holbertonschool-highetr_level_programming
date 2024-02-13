#!/usr/bin/python3
"""Pascal triangle module"""


def pascal_triangle(n):
    """Generates Pascal's triangle up to n levels.

    Args:
        n (int): The number of levels to generate in the triangle.

    Returns:
        list: A list of lists, where each sublist represents a
        level of Pascal's triangle.
    """
    triangle = []
    if n <= 0:
        return triangle

    """base du triangle"""
    triangle.append([1])
    """pour chaque rangé"""
    for i in range(1, n):
        """on commence par 1"""
        row = [1]
        for y in range(1, i):
            """on rempli le milieu en additionnant
            celui d'en haut et a sa gauche"""
            row.append(triangle[i-1][y-1] + triangle[i-1][y])
        """on fini par 1"""
        row.append(1)
        """on rajoute la rangé au triangle"""
        triangle.append(row)

    return triangle
