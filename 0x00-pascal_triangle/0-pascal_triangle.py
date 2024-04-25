#!/usr/bin/python3
"""runing pascal triangle"""


def pascal_triangle(n):
    """run pascal"""
    array = []
    for i in range(n):
        array.append(list(str(11**i)))
    return array
