from utils import palindromes_of_length

TOP = 100000000

def is_palindrome(n):
    return str(n) == str(n)[::-1]

palindromes = set(palindromes_of_length(8))
sums = set()

for i in xrange(1,int(TOP**0.5)+5):
    total = i*i
    for j in xrange(i+1, TOP):
        total += j*j

        if total >= TOP:
            break

        sums.add(total)

print(sum(list(palindromes & sums)))
