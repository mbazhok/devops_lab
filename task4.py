#!/usr/bin/env python


def dojob(num):

    if num < 10:
        return num + 10

    guess = []
    for delim in range(9, 1, -1):
        while num % delim == 0:
            num = num / delim
            guess.append(delim)

    if len(guess) < 2:
        return -1

    guess.sort()

    res = ''
    for i in guess:
        res += str(i)

    return int(res)
