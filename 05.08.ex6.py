given_txt_file = open("text.txt", "rt+")
words = given_txt_file.read().split()

count_dict = {}

for item in words:
    if count_dict.get(item) is None:
        count_dict[item] = 1
    else:
        count_dict[item] = int(count_dict[item]) + 1

print(count_dict)
