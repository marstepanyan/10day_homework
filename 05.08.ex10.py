def odd_nums(n1, n2):
    count = 0
    for i in range(n1, n2 + 1):
        if i % 2 != 0:
            count += 1
    return count


num1 = 3
num2 = 7
print(odd_nums(num1, num2))
