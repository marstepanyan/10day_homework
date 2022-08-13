def even(n):
    return n % 2 == 0


def beginning_even(arr):
    for j in range(len(arr)):
        for i in range(len(arr) - 1 - j):
            if not even(arr[i]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


lst1 = [11, 0, 2, 3, 5, 6, 7]
print(beginning_even(lst1))
