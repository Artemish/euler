from __future__ import print_function
from fractions import Fraction

def ways(n):
    if (n % 2) == 0:
        no_carry, carry = (1,1)
    else:
        no_carry, carry = (1,0)

    number = map(int, bin(n)[2:][::-1])

    for i in number[1:]:
        if i == 0:
            carry, no_carry = (no_carry + carry, no_carry)
        elif i == 1:
            carry, no_carry = (carry, no_carry + carry)

    return no_carry

a = 987654321 // 9
b = 123456789 // 9

# a, b = 13, 17

s = ""

while True:
    if (a == 1):
        print(b)
        # print("{} zeros, then ".format(b) + s[::-1])
        break

    if (b == 1):
        print(a)
        # print("{} ones, then ".format(a) + s[::-1])
        break

    if a < b:
        s += "0"
        a, b = a, b - a
    elif a > b:
        s += "1"
        a, b = a - b, b

print(s)
