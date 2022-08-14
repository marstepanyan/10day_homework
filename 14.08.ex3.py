def contains_duplicate(lst):
    return len(lst) != len(set(lst))


nums = [0, 1, 2, 3, 3, 4]
print(contains_duplicate(nums))
