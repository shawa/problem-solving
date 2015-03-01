#!/usr/local/bin/python3
import itertools


def is_pow_2(n):
    if n == 1:
        return True
    return (n & n-1 == 0)


def digit_perms(n):
    digits = str(n)
    return filter(lambda x: x != n or True, (int(''.join(s)) for s in itertools.permutations(digits)))


def main(args):
    limit = int(args[1])
    power_combinations = (digit_perms(2 **n) for n in range(limit))

    for power_combination in power_combinations:
        for number in power_combination:
            if is_pow_2(number):
                print(number)

if __name__ == '__main__':
    import sys
    args = [None, 10]
    main(sys.argv if len(sys.argv) > 1 else args)
