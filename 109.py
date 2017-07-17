from collections import defaultdict
from itertools import combinations_with_replacement

strike_outs = defaultdict(int)

singles = range(1,21) + [25]
doubles = map(lambda x:x*2, range(1,21) + [25])
triples = map(lambda x:x*3, range(1,21))

# 1 dart
for d in doubles:
    strike_outs[d] += 2

# 2 darts
for hit in singles + doubles + triples:
    for d in doubles:
        strike_outs[hit + d] += 2

for l1, l2 in combinations_with_replacement([singles,doubles,triples], 2):
    for h1 in l1:
        for h2 in l2:
            for d in doubles:
                if l1 == l2 and h1 != h2:
                    strike_outs[h1 + h2 + d] += 1
                else:
                    strike_outs[h1 + h2 + d] += 2

print(sum([strike_outs[i] for i in range(100)]) / 2)
