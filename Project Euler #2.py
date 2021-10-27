import time
start = time.time()


def fibonacci_sum(upper_bound):
    a, b, even_fibonacci_sum = 2, 1, 2
    while a < upper_bound:
        a, b = a + b, a
        if a % 2 == 0:
            even_fibonacci_sum += a
    return even_fibonacci_sum


result = fibonacci_sum(4000000)
end = time.time()
print(end - start)
print(result)
