#!/usr/bin/python3
'''Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
'''
import sys


def makeChange(coins, total):
    '''
    Determine the minimum number of coins needed to meet a given amount total.
    If total is 0 or less, return 0. If total cannot be met by any number of coins, return -1.

    Parameters:
    coins (list): A list of integers representing the values of available coins.
    total (int): The target amount to achieve using the fewest number of coins.

    Returns:
    int: The minimum number of coins needed to make up the total, or -1 if it's not possible.
    '''
    if total <= 0:
        return 0

    # Create a list to store the minimum number of coins for each amount from 0 to total
    dp = [sys.maxsize] * (total + 1)
    dp[0] = 0  # Zero coins are needed to make the amount zero

    # Iterate over each coin in the given list
    for coin in coins:
        # For each coin, update the dp array for all amounts that can be reached with this coin
        for amount in range(coin, total + 1):
            if dp[amount - coin] != sys.maxsize:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still sys.maxsize, it means the total cannot be made up with the given coins
    return dp[total] if dp[total] != sys.maxsize else -1


# Main function for testing the makeChange function
if __name__ == "__main__":
    # Example test cases
    print(makeChange([1, 2, 25], 37))  # Expected output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
