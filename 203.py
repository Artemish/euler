from collections import Counter
from utils import cheese_factor, n_choose_k

squarefree = set([1])

factor_lookup = [None, Counter([])]

for i in range(2, 52):
    factor_lookup.append(Counter(cheese_factor(i)) + factor_lookup[-1])

for i in range(2, 51):
    i_counter = factor_lookup[i]
    for j in range(1, i // 2 + 1):
        new_c = i_counter - factor_lookup[j] - factor_lookup[i-j]
        if new_c.most_common()[0][1] == 1:
            squarefree.add(n_choose_k(i, j))

print(sum(squarefree))
