TOP = 100000000

def is_palindrome(n):
    return str(n) == str(n)[::-1]

palindromes = set()
both = set()

for num_prefix in range(1,10000):
    pre = str(num_prefix)
    rev = pre[::-1]

    palindromes.add(pre + rev)

    if len(pre) == 4:
        continue

    for i in range(10):
        palindromes.add(pre + str(i) + rev)

for i in xrange(1,TOP-1):
    if i % 1000000 == 0:
        print(i)

    total = i*i
    for j in xrange(i+1, TOP):
        total += j*j

        if total >= TOP:
            break

        if total in palindromes:
            both.add(total)
