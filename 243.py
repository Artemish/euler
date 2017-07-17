from utils import phi_field_direct

TOP = 100000000

phis = phi_field_direct(TOP)

print("Got phi field")

for i in range(2, TOP):
    if (phis[i] * 94744) < ((i - 1) * 15499):
        print(str(i))
        break
