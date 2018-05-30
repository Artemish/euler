from random import randint

TEST_RUNS = 10 ** 7

A2, A3, A4, A5 = range(4)

single_instances = 0

for _ in xrange(TEST_RUNS):
    state = [1,1,1,1]
    pieces = 4

    for i in range(1,15):
        if pieces == 1:
            single_instances += 1
            r = 0
        else:
            r = randint(0, pieces-1)

        for j, v in enumerate(state):
            if r < v:
                state[j] -= 1
                pieces = (pieces - 1) + (3 - j)
                for k in xrange(j+1, 4):
                    state[k] += 1
                break
            else:
                r -= v

print(single_instances / (1.0 * TEST_RUNS))
