from utils import phi_field

TOP = 10**8

phis = phi_field(TOP+1)

print("Calculated phis")

total = TOP - 1
total += sum(((n - phis[n] - 1) for n in xrange(2, TOP+1)))

print(total * 6)
