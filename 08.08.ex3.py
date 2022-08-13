# not finished
def shortest_subarray(arr):
    degree = max(arr.count(item) for item in arr)
    indexes = [i for i, item in enumerate(arr) if arr.count(item) == degree]
    right_index = indexes[-1]
    left_index = indexes[0]
    # print(arr[left_index:right_index + 1])
    return len(arr[left_index:right_index + 1])


nums = [1, 2, 2, 1, 0, 2, 3]
print(shortest_subarray(nums))
