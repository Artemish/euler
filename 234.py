from primes import primes1

TOP = 999966663333
TOP_ROOT = int(TOP ** 0.5) + 1000

def get_first(bottom, top):
    return (((bottom*bottom) // top) + 1) * top

primes = primes1(TOP_ROOT)

total = 0

for i in xrange(len(primes) - 1):
    bottom, top = primes[i], primes[i+1]
    excluded = set([bottom*bottom, top*top])

    lower = bottom*bottom
    upper = min(top*top, TOP+1)

    bottom_set = set(xrange(lower, upper, bottom))

    top_start = get_first(bottom, top)
    top_set = set(xrange(top_start, upper, top))

    total += sum(top_set - (bottom_set | excluded))
    total += sum(bottom_set - (top_set | excluded))

print(total)
