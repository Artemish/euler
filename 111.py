from itertools import product, combinations
from collections import defaultdict
from utils import naive_prime_check

MNS = defaultdict(int)

def number_gen(digit, places):
    if digit == 0 and 9 in places:
        raise StopIteration

    free_places = [i for i in range(10) if i not in places]
    base = sum([digit * (10 ** place) for place in places])
    other_digits = range(10)
    other_digits.remove(digit)

    if len(free_places) == 0:
        yield sum([digit * (10 ** p) for p in range(10)])
        raise StopIteration

    zero_flag = 9 in free_places

    for digit_choices in product(other_digits, repeat=len(free_places)):
        if digit_choices[-1] == 0 and zero_flag:
            continue

        aux = base
        for p, d in zip(free_places, digit_choices):
            aux += d * (10 ** p)
        yield aux

cleared = set()

for i in range(9, 0, -1):
    for digit in range(0,10):
        if digit in cleared:
            continue

        for picked_places in combinations(range(10), i):
            for number in number_gen(digit, picked_places):
                if naive_prime_check(number):
                    cleared.add(digit)
                    MNS[digit] += number
