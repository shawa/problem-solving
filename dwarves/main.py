#!/usr/local/bin/python3
import math
from itertools import permutations


def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac


def valid(nums):
    # come on, you should really parametrise this
    a, b, c, d, e, f, g = nums
    return ((a > b and b < c and c > d and d < e and e > f and f < g) or
            (a < b and b > c and c < d and d > e and e < f and f > g))


def nCr(n, r):
    f = math.factorial
    return (f(n) / f(r)) / f(n-r)


def P(n):
    if n <= 1:
        return 2
    a = (1 / 4) * sum([nCr(n-1, k) * P(k) * P((n-1) - k) for k in range(n-1)])
    return int(a)


ds = range(7)
valid_arrangments = (lineup for lineup in permutations(ds) if valid(lineup))
n_arrangements = len(list(valid_arrangments))
decomp = primes(n_arrangements)

print(n_arrangements, decomp)
for vals in [(x, P(x)) for x in range(10)]:
    print(*vals)

