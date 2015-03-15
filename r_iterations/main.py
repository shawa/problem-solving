#!/usr/local/bin/python3
"""
usage: main.py <r> <x>
"""

from fractions import Fraction


def apply(r, f, x):
    """ return r iterations of f applied to x """
    for i in range(r):
        x = f(x)
    return x


def main(r, x):
    def f(x):
        return Fraction(1, 1-x)
    print(apply(r, f, x))


if __name__ == '__main__':
    import docopt
    args = docopt.docopt(__doc__)

    r = int(args['<r>'])
    x = int(args['<x>'])

    main(r, x)
