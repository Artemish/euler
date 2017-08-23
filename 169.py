no_carry, carry = (1,1)

number = map(int, bin(10**25)[2:][::-1])

for i in number[1:]:
    if i == 0:
        carry, no_carry = (no_carry + carry, no_carry)
    elif i == 1:
        carry, no_carry = (carry, no_carry + carry)

print(no_carry)
