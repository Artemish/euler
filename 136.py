from collections import defaultdict

# 4a - 1 <= n < 4a^2

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def test_a_n(a, n):
    a *= -1
    x = -3 * a + isqrt(4*a*a - n)
    y = x + a
    z = x + a + a
    print("Testing {}^2 - {}^2 - {}^2 = {}".format(x,y,z, n))

    if (x*x - y*y - z*z) != n:
        print("\tBad!")

TOP = 100

squares_upto = set([x*x for x in range(0, int(TOP ** 0.5) + 10)])

compatible_ns = defaultdict(list)

for a in range(1, (TOP - 1) / 4 + 2):
    for n in range(4*a-1, min(4*a*a, TOP) + 1): 
        if (4*a*a - n) in squares_upto:
            test_a_n(a, n)
            compatible_ns[a].append(n)

n_counts = defaultdict(int)

for a in compatible_ns:
    n_list = compatible_ns[a]
    for n in n_list:
        n_counts[n] += 1

t1 = 0
n1s = []

for n in range(1,TOP+1):
    if n_counts[n] == 1:
        n1s.append(n)
        t1 += 1

print("=============================")

t2 =  0
n2s = []

for n in range(1,TOP+1):
    low_a = (n + 1) / 4
    high_a = int(n ** 0.5) / 2 + 1
    t = 0
    for a in range(1, 1000):
        v = (4*a*a - n)
        if (isqrt(v) ** 2) == v:
            t += 1
            test_a_n(a, n)
            if (4*a - 1) > n or (4*a*a < n):
                print("Uh oh, a:{}, n:{}".format(a,n))

    if (t == 1):
        t2 += 1
        n2s.append(n)

print([n for n in n1s if n not in n2s])
print(t1)
print([n for n in n2s if n not in n1s])
print(t2)
