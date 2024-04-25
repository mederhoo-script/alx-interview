#!/usr/bin/python3


def pascal_triangle(n):
    if n <= 0:
        return []
    array = []
    for i in range(n):
        array.append(list(str(11**i)))
    return array
