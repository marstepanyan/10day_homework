# not finished
def shortest_subarray(arr):
    degree = max(arr.count(item) for item in arr)
    indexes = [i for i, item in enumerate(arr) if arr.count(item) == degree]

    unique_idx = []
    for item in arr:
        if arr.index(item) in indexes and arr.index(item) not in unique_idx:
            unique_idx.append(arr.index(item))

    left_idx = max(unique_idx)
    key = arr[left_idx]
    right_idx = len(arr) - 1 - arr[::-1].index(key)
    # print(arr[left_idx:right_idx + 1])
    return len(arr[left_idx:right_idx + 1])


nums = [1, 2, 2, 1, 0, 2, 3]
print(shortest_subarray(nums))
