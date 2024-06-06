#!/usr/bin/python3
'''N Queens Challenge Solution'''

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if board_size < 4:
        print('N must be at least 4')
        exit(1)

    solutions_list = []
    current_queens = []  # positions of queens in [row, column] format
    stop_flag = False
    row = 0
    column = 0

    # Iterate through rows
    while row < board_size:
        step_back = False
        # Iterate through columns
        while column < board_size:
            # Check if current column is safe for the queen
            is_safe = True
            for queen_position in current_queens:
                col = queen_position[1]
                if (col == column or col + (row - queen_position[0]) ==
                    column or
                        col - (row - queen_position[0]) == column):
                    is_safe = False
                    break

            if not is_safe:
                if column == board_size - 1:
                    step_back = True
                    break
                column += 1
                continue

            # Place the queen
            new_position = [row, column]
            current_queens.append(new_position)
            # If last row is reached, store the solution
            if row == board_size - 1:
                solutions_list.append(current_queens[:])
                for queen_position in current_queens:
                    if queen_position[1] < board_size - 1:
                        row = queen_position[0]
                        column = queen_position[1]
                for i in range(board_size - row):
                    current_queens.pop()
                if row == board_size - 1 and column == board_size - 1:
                    current_queens = []
                    stop_flag = True
                row -= 1
                column += 1
            else:
                column = 0
            break
        if stop_flag:
            break
        # If failed to place a queen, backtrack to the previous row
        # and continue from the last safe column + 1
        if step_back:
            row -= 1
            while row >= 0:
                column = current_queens[row][1] + 1
                del current_queens[row]  # Remove the queen from position
                if column < board_size:
                    break
                row -= 1
            if row < 0:
                break
            continue
        row += 1

    for idx, val in enumerate(solutions_list):
        if idx == len(solutions_list) - 1:
            print(val, end='')
        else:
            print(val)
