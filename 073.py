from fractions import gcd

total = 0

for d in range(2,12001):
    for n in range(d/3,d/2+1):
        g = gcd(n,d)
        if g != 1:
            continue
        if (n * 3 > d) and (n * 2 < d):
            total +=1

print("found " + str(total))
