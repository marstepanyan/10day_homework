def selection_sort(lst):
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst


lst1 = [3, 0, 7, 1, 5]
print(selection_sort(lst1))
