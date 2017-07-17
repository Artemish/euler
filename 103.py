def n_sets_of_sum(n, total, top=True):
    if n == 0:
        yield set()
        return

    minimum = 1
    maximum = (total / n) - sum(range(n))
    for new_element in range(minimum, maximum + 1, top=False):
        for remaining in n_sets_of_sum(n - 1, total - new_element):
            yield set([new_element]) | remaining


