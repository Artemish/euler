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


primes = primes_below(100000)
viable_primes = filter(lambda p: only_wanted(cycle(p)), primes)
nonviable_primes = set(primes) - set(viable_primes)

print(sum(nonviable_primes) + 2 + 5)
