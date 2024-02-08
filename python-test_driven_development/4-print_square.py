#!/usr/bin/python3
"""Print a square"""


def print_square(size):
    """Initialize to print a square

        Args:
                size (int): size of square

        Raises:
                TypeError: size is not integer
                ValueError: size must be positive
        """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for height in range(size):
        print("#" * size)
