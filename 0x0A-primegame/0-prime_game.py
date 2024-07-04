#!/usr/bin/python3
'''Prime Game'''


def isWinner(x, nums):
    '''Determines the overall winner'''
    scoreCounter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        winnerOfRound = determineRoundWinner(nums[i], x)
        if winnerOfRound is not None:
            scoreCounter[winnerOfRound] += 1

    if scoreCounter['Maria'] > scoreCounter['Ben']:
        return 'Maria'
    elif scoreCounter['Ben'] > scoreCounter['Maria']:
        return 'Ben'
    else:
        return None


def determineRoundWinner(n, x):
    '''Determines the winner of a single round'''
    numberList = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        currentPlayer = players[i % 2]
        markedIndices = []
        primeNumber = -1
        for idx, num in enumerate(numberList):
            # If a prime number has been picked, mark its multiples
            if primeNumber != -1:
                if num % primeNumber == 0:
                    markedIndices.append(idx)
            # Otherwise, find the next prime number
            else:
                if isPrime(num):
                    markedIndices.append(idx)
                    primeNumber = num
        # If no prime number can be picked, the current player loses
        if primeNumber == -1:
            if currentPlayer == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            for idx, val in enumerate(markedIndices):
                del numberList[val - idx]
    return None


def isPrime(n):
    # 0, 1, and even numbers greater than 2 are NOT PRIME
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        # Not prime if divisible by any number less than
        # or equal to the square root of itself.
        for i in range(3, int(n**(1/2))+1, 2):
            if n % i == 0:
                return "Not prime"
        return True
