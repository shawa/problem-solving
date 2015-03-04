#!/usr/local/bin/python3
import random
import itertools

point = lambda: (random.random(), random.random())
m = lambda a, b: (b[1] - a[1]) / (b[0] - a[0])
c = lambda a, b: a[1] - m(a, b) * a[0]
f = lambda a, b: lambda x: m(a, b) * x + c(a, b)

a = point()
b = point()

points = (point() for _ in range(10))
pairs = itertools.product(points, repeat=2)
funcs = map(f, pairs)

print(list(pairs))
