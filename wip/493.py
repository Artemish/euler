from collections import Counter
from utils import ncr
from math import factorial

def color_gen(remaining, drawn_list, upper_bound):
    remaining_colors = 7 - len(drawn_list)

    if remaining_colors * upper_bound < remaining:
        return
    elif remaining == 0:
        yield drawn_list

    if remaining_colors == 1:
        yield drawn_list + [remaining]

    for number_added in range(1, min(upper_bound, remaining) + 1): 
        for x in color_gen(remaining - number_added,
                           drawn_list + [number_added],
                           min(number_added, upper_bound)):
            yield x

total = 0
possibilities = 0

for drawing in color_gen(20, [], 10):
    c = Counter(drawing)
    uniques = 0
    occurrences = 1

    for i in range(1,11):
        if c[i] > 0:
            uniques += 1
            occurrences *= ncr(10, c[i])

    total += occurrences * uniques
    possibilities += occurrences

print((total * 1.0) / possibilities)
