lst = [3, 7, 13, 6, 7, 3, 4, 7, 13]

count_dict = {}

for item in lst:
    if count_dict.get(item) is None:
        count_dict[item] = 1
    else:
        count_dict[item] = int(count_dict[item]) + 1

print(count_dict)
