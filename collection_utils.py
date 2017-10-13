def split_set_generator(s):
    l = len(s)

    if (l % 2) == 0:
        for i in range(1, l / 2):
            for first_tuple in combinations(s, i):
                first_set = set(first_tuple)
                second_set = s - first_set
                yield first_set, second_set

        for first_tuple in combinations(s, l / 2):
            first_set = set(first_tuple)
            second_set = s - first_set
            if first_tuple > tuple(second_set):
                return

            yield first_set, second_set

    else:
        for i in range(1, l / 2 + 1):
            for first_tuple in combinations(s, i):
                first_set = set(first_tuple)
                second_set = s - first_set
                yield first_set, second_set

def distinct_permutations(l):
    c = Counter(l)
    vs = c.values()
    permutations = math.factorial(sum(vs))
    return reduce(lambda perms, v: perms // math.factorial(v), vs, permutations)

def list_powerset(lst):
    result = [[]]
    for x in lst:
        result.extend([subset + [x] for subset in result])
    return result

def powerset(s):
    return frozenset(map(frozenset, list_powerset(list(s))))
