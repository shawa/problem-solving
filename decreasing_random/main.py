#!/usr/local/bin/python3
import random


def random_decreasing():
    prev = random.random()
    yield prev
    next = random.random()
    while next < prev:
        yield next
        prev = next
        next = random.random()
    else:
        yield next


def take_sample(_):
    return sum(1 for _ in random_decreasing())


def main(args):
    n_trials = int(args[1]) if len(args) > 1 else 100000
    avg = sum(map(take_sample, range(n_trials))) / n_trials
    print(avg)


if __name__ == '__main__':
    import sys
    main(sys.argv)
