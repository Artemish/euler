from utils import powerset
from itertools import combinations

def test(s):
    all_subsets = powerset(s)

    for (s1, s2) in combinations(all_subsets, 2):
        if s1 == s2:
            continue

        if len(s1) > len(s2) and sum(s1) <= sum(s2):
            return False
        elif len(s2) > len(s1) and sum(s2) <= sum(s1):
            return False
        elif sum(s1) == sum(s2):
            return False

    return True

for c in combinations(xrange(20, 45), 7):
    s = set(c)
    if test(s):
        print(''.join(map(str, c)))
        break
