given_num_file = open("numbers.txt", "rt+")

lines = given_num_file.readlines()
sum_of_nums = 0

for line in lines:
    for item in line:
        if item.isdigit() is True:
            sum_of_nums += int(item)

print(sum_of_nums)
