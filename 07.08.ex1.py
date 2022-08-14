def square_of_sum(n):
    return ((n * (n + 1)) // 2) ** 2


def sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6


print(sum_of_squares(100) - square_of_sum(100))
