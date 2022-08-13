def is_part_of(str1, str2):
    if str2 == '':
        return 0
    if str2 not in str1:
        return -1
    for i in range(len(str1) - len(str2) + 1):
        if str1[i] == str2[0]:
            if str1[i:i + len(str2)] == str2:
                return i


haystack = "a"
needle = "a"
print(is_part_of(haystack, needle))
