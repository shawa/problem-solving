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


def take_sample():
    return len(list(random_decreasing()))


def serial_samples(n_trials):
    return (take_sample() for _ in range(n_trials))


def main(args):
    n_trials = int(args[1]) if len(args) > 1 else 100000

    summation = 0
    for x in (serial_samples(n_trials)):
        summation += x

    avg = summation / n_trials
    print(avg)


if __name__ == '__main__':
    import sys
    main(sys.argv)
