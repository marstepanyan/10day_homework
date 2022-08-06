def str_move(txt, n):
    res = " "
    res += txt[-n:] + txt[:-n]
    return res


txt_ = 'Hello'
num = 2
print(str_move(txt_, num))
