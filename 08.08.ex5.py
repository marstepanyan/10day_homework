def sum_of_uniques(arr):
    sum_ = 0
    for item in arr:
        if arr.count(item) == 1:
            sum_ += item
    return sum_


nums = [2, 3, 3, 4, 5]
print(sum_of_uniques(nums))
