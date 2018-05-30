big_matrix = [\
[  7, 53,183,439,863,497,383,563, 79,973,287, 63,343,169,583],
[627,343,773,959,943,767,473,103,699,303,957,703,583,639,913],
[447,283,463, 29, 23,487,463,993,119,883,327,493,423,159,743],
[217,623,  3,399,853,407,103,983, 89,463,290,516,212,462,350],
[960,376,682,962,300,780,486,502,912,800,250,346,172,812,350],
[870,456,192,162,593,473,915, 45,989,873,823,965,425,329,803],
[973,965,905,919,133,673,665,235,509,613,673,815,165,992,326],
[322,148,972,962,286,255,941,541,265,323,925,281,601, 95,973],
[445,721, 11,525,473, 65,511,164,138,672, 18,428,154,448,848],
[414,456,310,312,798,104,566,520,302,248,694,976,430,392,198],
[184,829,373,181,631,101,969,613,840,740,778,458,284,760,390],
[821,461,843,513, 17,901,711,993,293,157,274, 94,192,156,574],
[ 34,124,  4,878,450,476,712,914,838,669,875,299,823,329,699],
[815,559,813,459,522,788,168,586,966,232,308,833,251,631,107],
[813,883,451,509,615, 77,281,613,459,205,380,274,302, 35,805],]

DIM = 15

test_matrix = \
[[  7,  53, 183, 439, 863],
 [497, 383, 563,  79, 973],
 [287,  63, 343, 169, 583],
 [627, 343, 773, 959, 943],
 [767, 473, 103, 699, 303]]

col_taken = set()
row_taken = set()

total = 0

for i in range(DIM//2):
    min_x, min_y, min_v = 0, 0, 1000
    for row in set(range(DIM)) - row_taken:
        for col in set(range(DIM)) - col_taken:
            if big_matrix[row][col] < min_v:
                min_x, min_y, min_v = col, row, big_matrix[row][col]

    print("Found mins {}@({},{})".format(min_v, min_x, min_y))

    cols = filter(lambda x: x[0] not in col_taken, enumerate(big_matrix[min_y]))
    rows = filter(lambda x: x[0] not in row_taken, enumerate([big_matrix[row][min_x] for row in range(DIM)]))

    print(cols)
    print(rows)

    max_row, max_row_v = max(rows, key=lambda x: x[1])
    max_col, max_col_v = max(cols, key=lambda x: x[1])

    print("Taking col {}:{}".format(max_col, max_col_v))
    col_taken.add(max_col)
    row_taken.add(min_y)

    print("Taking row {}:{}".format(max_row, max_row_v))
    row_taken.add(max_row)
    col_taken.add(min_x)

    total += max_col_v
    total += max_row_v

final_row = list(set(range(DIM)) - row_taken)[0]
final_col = list(set(range(DIM)) - col_taken)[0]

print(total + big_matrix[final_row][final_col])
