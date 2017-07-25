from utils import square_root_cf

total = 0
for i in range(2,10001):
    root = int(i ** 0.5)
    if root * root == i:
        continue

    _, repeated = square_root_cf(i)
    if len(repeated) % 2 == 1:
        total += 1

print(total)
