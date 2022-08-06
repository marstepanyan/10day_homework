def sum_of_multiples(n):
    lst = []
    for number in range(n):
        if number % 3 == 0 or number % 5 == 0:
            lst.append(number)
    return sum(lst)


print(sum_of_multiples(1000))
