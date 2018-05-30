from collections import defaultdict

path_sums = defaultdict(lambda: defaultdict(int))

for i in range(10):
    path_sums[(1, i)][(0,0,i)] = 1

for d in range(2,5):
    for i in range(10):
        for (pre3,pre2,pre1) in path_sums[(d-1,i)]:
            paths = path_sums[(d-1,i)][(pre3,pre2,pre1)]

            for to_add in range(10-pre1-pre2):
                path_sums[(d,i + to_add)][(pre2,pre1,to_add)] += paths

four_data = []

for a in range(10):
    for b in range(10-a):
        for c in range(10-a-b):
            for d in range(10-b-c):
                four_data.append(1000 * a + 100*b + 10*c + d)
