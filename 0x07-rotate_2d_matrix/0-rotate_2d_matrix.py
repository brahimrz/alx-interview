#!/usr/bin/python3
""" Rotate 2d
"""


def rotate_2d_matrix(matrix):
    """ Given an n x n  rotate it 90 degrees clockwise
    """
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    """ roe """
    rotate_2d_matrix(matrix)
    print(matrix)
