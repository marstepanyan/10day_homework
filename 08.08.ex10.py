def position(arr, n):
    if n not in arr:
        return[-1, -1]
    indexes = [i for i, item in enumerate(arr) if item == n]
    return [indexes[0], indexes[-1]]


nums = [5, 7, 7, 8, 8, 3, 8, 10]
target = 8
print(position(nums, target))
