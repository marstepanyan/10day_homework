def difference(n):
    return mult_of_digits(n) - sum_of_digits(n)


def sum_of_digits(n):
    result = 0
    for digit in str(n):
        result += int(digit)
    return result


def mult_of_digits(n):
    res = 1
    for digit in str(n):
        res *= int(digit)
    return res


num = 4637
print(difference(num))
