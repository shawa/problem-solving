#!/usr/local/bin/python3


def adjacents(n):
    return {1, 2, 3, 4, 5, 6} - {7-n}


def average(cube, face, neighbours):
    return sum(cube[i] for i in neighbours) / len(neighbours)


def cube_iteration(cube):
    averages = {x: average(cube, x, adjacents(x)) for x in cube}
    return averages


def cube_iters(cube):
    res = cube
    while True:
        res = cube_iteration(res)
        yield res


def nth_cube(cube):
    def nth_rec(cube, n):
        if n == 0:
            return cube
        else:
            return nth_rec(cube, n-1)

    return nth_rec(cube)


def main(args):
    try:
        n = int(args[1])
        output_iterations = args[2] == 'print'
    except IndexError:  # hurr defaults
        n = 100
        output_iterations = False

    cube = {i: i for i in range(1, 7)}
    vals = cube_iters(cube)

    for x in range(n):
        val = next(vals)
        if output_iterations:
            print(val)

    if not output_iterations:
        print(val)

if __name__ == '__main__':
    import sys
    main(sys.argv)
