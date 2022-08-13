def palindrome(s):
    new_s = (''.join(filter(str.isalnum, s))).lower()
    # print(s)
    return new_s == new_s[::-1]


string_value = "A man, a plan, a canal: Panama"
print(palindrome(string_value))
