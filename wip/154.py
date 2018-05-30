TOP = 200000

def two_five_counter(n):
    v = 2
    twos = 0
    while (v <= n):
        twos += (n // v)
        v *= 2

    v = 5
    fives = 0
    while (v <= n):
        fives += (n // v)
        v *= 5

    return (twos, fives)

values = map(two_five_counter, range(0, TOP + 1))
all_2s, all_5s = values[TOP]

num_uniques = 0
for i in range(TOP // 3):
    print(i)
    i2, i5 = values[i]
    for j in range(i+1,(TOP-i)//2):
        k = TOP - i - j

        j2,j5 = values[j]
        k2,k5 = values[k]

        if (i2+j2+k2+12 <= all_2s) and (i5+j5+k5+12 <= all_5s):
            num_uniques += 1

num_twosame = 0
for i in range(TOP // 2):
    i2, i5 = values[i]

    j = i
    j2, j5 = values[j]

    k = TOP - i - j
    k2,k5 = values[k]

    if (i2+j2+k2+12 <= all_2s) and (i5+j5+k5+12 <= all_5s):
        num_twosame += 1
