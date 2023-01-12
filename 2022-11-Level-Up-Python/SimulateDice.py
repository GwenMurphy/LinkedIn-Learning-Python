"""
Challenge:      Write a Python function to determine the probability of certain outcomes when rolling dice.

Input:          Variable number of arguments for sides of dice.

Output:         Table of probability for each possible outcome.
"""


##### ##### Instructor's solution

from random import randint
from collections import Counter

def roll_dice(*dice, num_trials=1_000_000):
    counts = Counter()
    for _ in range(num_trials):
        counts[sum((randint(1, sides) for sides in dice))] += 1

    print('\nOUTCOME\tPROBABILITY')
    for outcome in range(len(dice), sum(dice) + 1):
        print(f'{outcome}\t{counts[outcome] * 100 / num_trials :0.2f}%')