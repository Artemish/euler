def H(n):
    total = 0
    side_len = 1
    hex_len = 1
    while side_len * 3 <= n:
        space_depth = (n - 3 * side_len) + 1
        total += (space_depth * space_depth + space_depth) // 2
        # print("Normal: {}: {} -> {}".format(n, side_len, space_depth))
        side_len += 1

    order = 1
    while 6 * order <= n:
        space_depth = n - (6 * order) + 1
        total += (space_depth * space_depth + space_depth) // 2
        # print("Ordered: {}: {} -> {}".format(n, order, space_depth))
        order += 1

    return total
