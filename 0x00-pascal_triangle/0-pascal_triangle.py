#!/usr/bin/python3
"""
This module contains a function that returns a list of lists of integers
representing Pascal's triangle of n rows.
"""

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n rows.

    Args:
        n (int): Number of rows in Pascal's triangle.

    Returns:
        list: A list of lists, where each list represents a row of Pascal's triangle.
    """
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first row
    triangle = [[1]]

    # Generate each row of Pascal's triangle
    for i in range(1, n):
        row = [1]  # Start each row with a 1
        for j in range(1, i):
            # Calculate the value based on the two elements above
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with a 1
        triangle.append(row)

    return triangle
