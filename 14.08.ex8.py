def is_prime(num):
    if num > 1:
        for i in range(2, num // 2):
            if num % i == 0:
                return False
        return True


def largest_prime_factor(num):
    if is_prime(num):
        return num

    prime_factors = []
    for i in range(num):
        if is_prime(i) and num % i == 0:
            prime_factors.append(i)
    # print(prime_factors)
    return max(prime_factors)


print(largest_prime_factor(13195))
