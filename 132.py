from factoring import primes_below

def cycle(p):
  x = 1
  seen = set()
  while x not in seen:
    seen.add(x)
    x = (x*10 + 1) % p
  return len(seen)

def only_wanted(n):
  while (n % 5) == 0:
    n /= 5
  while (n % 2) == 0:
    n /= 2
  return (n == 1)


primes = primes_below(500000)

viable_primes = []
for p in primes[3:]:
    cycle_len = cycle(p)
    if (10**9) % cycle_len == 0:
        print("Found " + str(p))
        viable_primes.append(p)
        if len(viable_primes) == 40:
            break

print(sum(viable_primes))
