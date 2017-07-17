from utils import phi_field_direct

phi = phi_field_direct(10000000)

min_ratio = 100.
min_i = -1

for i in range(2, 10000000):
    if (i % 100000) == 0:
        print("Hit {}".format(i))

    if sorted(str(i)) == sorted(str(phi[i])):
        if i * 1.0 / phi[i] < min_ratio:
            min_i = i
            min_ratio = i * 1.0 / phi[i]
        
print min_ratio, min_i
