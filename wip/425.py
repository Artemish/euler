from utils import primes_below
import sys

sys.setrecursionlimit(10000)

TOP = 10**4

primes = primes_below(TOP)
prime_set = set(primes)

smallest_max = {p: TOP for p in primes}

def dfs_visit(p, relatives, biggest):
    biggest = max(biggest, p)
    if p >= biggest:
        relatives.add(p)

    for digit in range(len(str(p))):
        string = list(str(p))
        base = int(string[digit])
        for replacement in range(10):
            string[digit] = str(replacement)
            neighbor = int(''.join(string))
            if neighbor in prime_set and biggest < smallest_max[neighbor]:
                smallest_max[neighbor] = biggest
                dfs_visit(neighbor, relatives, max(neighbor, biggest))

    for prefix in range(1,10):
        neighbor = int("{}{}".format(prefix, p))
        if neighbor in prime_set and biggest < smallest_max[neighbor]:
            smallest_max[neighbor] = biggest
            dfs_visit(neighbor, relatives, max(neighbor, biggest))


relatives = set([2])
dfs_visit(2, relatives, 2)

left_out = prime_set - relatives
print(sum(left_out))
