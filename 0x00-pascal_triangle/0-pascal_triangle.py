#!/usr/bin/python3


def pascal_triangle(n):
    array = []
    for i in range(n):
        array.append(list(str(11**i)))
    return array
