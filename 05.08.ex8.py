def sum_of_digits(n):
    summa = 0
    for digit in str(n):
        summa += int(digit)
    return summa


num = 46371
print(sum_of_digits(num))
