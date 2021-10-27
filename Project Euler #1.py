import time
start = time.time()


def multiples_sum(a, b):
    c, a_sum, b_sum, c_sum = a*b, 0, 0, 0
    for x in range(a, 1000, a):
            a_sum += x
    for y in range(b, 1000, b):
            b_sum += y
    for z in range(c, 1000, c):
            c_sum += z
    return a_sum + b_sum - c_sum


multi_sum = multiples_sum(3, 5)
print(multi_sum)
end = time.time()
print(end - start)
