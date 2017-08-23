from utils import primes_below
from memoizers import key_memoized

T, TL, TR, M, BL, BR, B = range(7)

segs = [[T,TL,TR,BL,BR,B],
        [TR,BR],
        [T,TR,M,BL,B],
        [T,TR,M,BR,B],
        [TL,TR,M,BR],
        [T,TL,M,BR,B],
        [T,TL,M,BL,BR,B],
        [T,TL,TR,BR],
        [T,TL,TR,M,BR,BL,B],
        [T,TL,TR,M,BR,B]]

transitions = [[len(set(segs[i]) ^ set(segs[j])) for j in range(10)] for i in range(10)]

max_count = sam_count = 0

@key_memoized
def clock_counts(p, prev=None):
    s = sum([len(segs[int(i)]) for i in str(p)]) * 2

    p_str = str(p)

    if prev is None:
        m = sum([len(segs[int(i)]) for i in str(p)])
    else:
        prev_str = str(prev)

        to_turn_off = len(prev_str) - len(p_str)

        m = sum([len(segs[int(i)]) for i in prev_str[:to_turn_off]])

        for d in range(len(p_str)):
            d_prev = int(prev_str[d+to_turn_off])
            d_p = int(p_str[d])

            m += transitions[d_prev][d_p]

    if (p >= 10):
        root = sum(map(int, p_str))
        next_m, next_s = clock_counts(root, prev=p)
        m, s = m + next_m, s + next_s
    else:
        m += sum([len(segs[int(i)]) for i in str(p)])

    return m, s

for p in primes_below(2*(10**7)):
    if p < 10**7:
        continue

    m, s = clock_counts(p)
    max_count += m
    sam_count += s

print(sam_count - max_count)
