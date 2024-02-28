#!/usr/bin/python3
"""
The module that determine the fewest number of coins needed to meet a given
amount total for a given a pile of coins of different values
"""


def makeChange(coins, total):
    """ fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    """
    if total < 0:
        return 0
    coins.sort(reverse=True)
    coins_count = 0
    for coin in coins:
        if total <= 0:
            break
        b = total // coin
        coins_count += b
        total -= (b * coin)
    if total != 0:
        return -1
    return coins_count
