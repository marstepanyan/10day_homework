def merge(lst1, m, lst2, n):
    i = 0
    j = 0

    while i < (m + n) and j < n:
        if lst2[j] < lst1[i]:
            lst1.insert(i, lst1[-1])
            lst1.pop()
            lst1[i] = lst2[j]
            j += 1

        else:
            if i >= m + j:
                lst1.insert(i, lst1[-1])
                lst1.pop()
                lst1[i] = lst2[j]
                j += 1

            i += 1

    return lst1


nums1 = [2, 5, 6, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3
print(merge(nums1, m, nums2, n))
