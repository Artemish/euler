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

test_1 = set([81, 88, 75, 42, 87, 84, 86, 65])
test_2 = set([157, 150, 164, 119, 79, 159, 161, 139, 158])

total = 0

with open('p105_sets.txt') as f:
    for line in f:
        print("Testing ({})".format(line[:-1]))
        nums = map(int, line.split(','))
        s = set(nums)
        if test(s):
            total += sum(s)

print(total)
