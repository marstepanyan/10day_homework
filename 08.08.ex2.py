def intersection(arr1, arr2):
    res = []
    for item in arr1:
        if item in arr2 and item not in res:
            res.append(item)
    return res


nums1 = [7, 5, 25, 27, 33, 33]
nums2 = [7, 34, 27, 33, 33]
print(intersection(nums1, nums2))
