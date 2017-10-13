m = 1777
v = m

for i in range(1854):
    v = pow(m, v, 100000000)

print(v)
