from itertools import product
from operator import mul

def evaluate(l):
    return reduce(mul, map(lambda t: t[1] ** (t[0]+1), enumerate(l)))

def net_change(v, e, increment):
    return ((v+increment) / v) ** e

def bump(l, increment):
    biggest = 0.0
    index_pairs = product(range(len(l)), range(len(l)))
    for (i, j) in index_pairs:
        if (i >= j):
            continue
        i_change = net_change(l[i], i+1, -1*increment)  
        j_change = net_change(l[j], j+1, increment)  
        change = i_change * j_change

        if change > 1.0 and change > biggest:
            biggest = change
            incremented = (i, j)

    if biggest != 0.0:
        return incremented


def trial(m, increment=1e-5):
    vals = [1.0] * m

    while True:
        incremented = bump(vals, increment)

        if incremented is None:
            return int(evaluate(vals))
        else:
            vals[incremented[0]] -= increment
            vals[incremented[1]] += increment

print(sum(map(trial, range(2,16))))
