def missing_number(lst):
    n = len(lst) + 1
    total_sum = n*(n-1) // 2
    return total_sum - sum(lst)


numbers = [3, 0, 1]
print(missing_number(numbers))
