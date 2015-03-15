#!/usr/local/bin/pypy3
import random
import sys


def sample():
    t = 0
    n = 0
    while t < 1:
        t += random.random()
        n += 1
    return n


n = int(sys.argv[1])
print(sum(sample() for _ in range(n)) / n)
