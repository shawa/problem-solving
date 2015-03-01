#!/usr/local/bin/python3

import operator
from functools import reduce

def sequence(filename):
    with open(filename, 'r') as f:
        sequence = [int(line.rstrip()) for line in f]
        return sequence


def pretty_print(iterable):
    for x in iterable:
        print(x)


def main(function):
    nums = sequence('seq.csv')
    pretty_print(map(function, nums))

    print(reduce(operator.mul, nums))


if __name__ == '__main__':
    main(bin)
