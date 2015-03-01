#!/usr/local/bin/python3
import matplotlib.pyplot as plt

def update_doubles(s, x):
    if x/2 < 1:
        return

    s.add(x//4)
    s.discard(x // 2)
    update_doubles(s, x // 4)


def sequence(n, coeff):
    numbers = set(range(n))
    for x in range(n):
        if x // 2 in numbers:
            update_doubles(numbers, x)

    return numbers


def plot_sequence(sequence):
    xs = list(sequence)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(0, max(sequence))
    ax.set_ylim(0, 2)

    for px in xs:
        plt.plot(px, 1, 'r.', mfc='r')

    lins = []
    for i, x in enumerate(xs):
        try:
            if (xs[i+1] - 1 != x) or (xs[i-1] + 1 != x):
                lins.append(x)
                plt.plot(x, 1, 'ro', mfc='r')
                ax.annotate(str(x), xy=(x-0.5, 0.5))
        except IndexError:
            continue

    ax.axes.get_yaxis().set_visible(False)
    ax.axis('off')
    plt.show()


def main(args):
    n = int(args[1])
    coeff = int(args[2])
    s = sequence(n, coeff)
    plot_sequence(s)

if __name__ == '__main__':
    import sys
    main(sys.argv)
