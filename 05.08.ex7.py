lst = [3, 7, 13, 6, 7, 3, 4, 13]
squares_lst = []

for item in lst:
    squares_lst.append(item ** 2)
    squares_lst.sort()

print(squares_lst)
