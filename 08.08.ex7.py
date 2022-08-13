def len_of_last_word(s):
    lst = s.split()
    # print(lst)
    return len(lst[-1])


str1 = "   fly me   to   the  moon  "
print(len_of_last_word(str1))
