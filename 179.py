from collections import defaultdict

factors = [[] for i in xrange(10**7)]

prev = -1

for i in xrange(2, 10**7):
    if len(factors[i]) == 0:
        for j in xrange(i, 10**7, i):
            factors[j].append(i)

total = 0
prev_d = -1
d = [0,1]

for i in xrange(2, 10**7):
    divs = 1
    x = i
    for f in factors[i]:
        e = 0
        while (x % f) == 0:
            e += 1
            x /= f
        divs *= (e + 1)

    d.append(divs)

    if (divs == prev_d):
        total += 1

    prev_d = divs

print(total)
