def is_palindrome(num):
    return str(num)[::-1] == str(num)


print(is_palindrome(121))

"""
def is_palindrome(num):
    res = 0
    n = num
    while n > 0:
        res = res * 10 + n % 10
        n = n // 10
    return num == res """
