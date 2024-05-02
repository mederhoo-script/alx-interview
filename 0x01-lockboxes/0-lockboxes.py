#!/usr/bin/python3
"""a method that determines if all the boxes
can be opened.
"""


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: if all boxes can be opened OR
        False: if not all boxes can be opened
    '''

    # Initialize a set to keep track of visited boxes
    visited = set()

    # Initialize a queue to perform BFS
    queue = [0]

    # Mark the first box as visited
    visited.add(0)

    # Perform BFS
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            # Check if the key opens a new box
            if key < len(boxes) and key not in visited:
                queue.append(key)
                visited.add(key)

    # If all boxes have been visited, return True, else return False
    return len(visited) == len(boxes)
