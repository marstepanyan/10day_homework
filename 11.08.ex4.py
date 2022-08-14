def merge_sort(lst):
    if len(lst) < 2:
        return lst

    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    i = 0       # for left
    j = 0       # for right
    k = 0       # for lst

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1

    return lst


lst2 = [12, 11, 13, 5, 33, 6, 7]
print(merge_sort(lst2))
