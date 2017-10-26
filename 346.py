strongs = set([1])

TOP = 10**12

for b in range(2, 10**6+1):
    i = 3
    v = ((b**i) - 1) // (b - 1)
    while v < TOP:
        strongs.add(v)
        i += 1
        v = ((b**i) - 1) // (b - 1)

print(sum(strongs))
