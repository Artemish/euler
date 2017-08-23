from collections import defaultdict
from math import log

TOP = 200

fastest = defaultdict(int)
for i in range(1,TOP+1):
    fastest[i] = i

# def hamming(n):
#     ones = 0
#     while n > 0:
#         if n & 1:
#             ones += 1
#         n = n >> 1
# 
#     return ones
# 
# def can_prine(length, n):
#     lhs = log(n, 2) + log(hamming(n), 2) - 2.2
#     pass

def recurse(l):
    length = len(l)
    if length > 16:
        return

    fastest[l[-1]] = min(fastest[l[-1]], length)

    for e in l[::-1]:
        v = l[-1] + e

        if length > (fastest[v] + 2) or (v > TOP):
            return

        recurse(l + [v])

recurse([1])
