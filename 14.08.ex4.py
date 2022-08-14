def single_number(lst):
    for item in lst:
        if lst.count(item) == 1:
            return item


nums = [0, 0, 1, 3, 3, 4]
print(single_number(nums))
