def max_consecutive_ones(lst):
    length = 0
    res = 0
    for item in lst:
        length = (length * item) + item
        res = max(length, res)
    return res


nums = [1, 1, 0, 0, 1, 1, 1, 0, 1]
print(max_consecutive_ones(nums))
