cache = [0, 1]


def fib(n):
    if n <= 2:
        return cache[n - 1]
    for i in range(2, n):
        fib_num = cache[i - 1] + cache[i - 2]
        cache.append(fib_num)
    # print(cache)
    return cache[n - 1]


num = 8
print(num, 'th Fibonacci number:', fib(num))
