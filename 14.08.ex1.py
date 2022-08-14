def remove_duplicates(lst):
    i = 0
    for j in range(1, len(lst)):
        if lst[i] != lst[j]:
            i += 1
            lst[i] = lst[j]
    # print(lst)
    return i + 1


nums = [0, 1, 1, 1, 2, 2, 3, 3, 4]
print(remove_duplicates(nums))
