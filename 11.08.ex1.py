def bubble_sort(lst):
    for i in range(len(lst)):
        swapped = False
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
                # print(lst)
        if swapped is False:
            break
    return lst


lst1 = [3, 0, 7, 1, 5]
print(bubble_sort(lst1))
