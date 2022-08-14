def pair_max_sum(lst):
    res = 0
    pairs = []
    lst = sorted(lst)
    for i in range(0, len(lst), 2):
        pairs.append(lst[i:i + 2])
    for pair in pairs:
        res += min(pair)

    return res


nums = [6, 2, 6, 5, 1, 2]
print(pair_max_sum(nums))
