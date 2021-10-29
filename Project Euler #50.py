import time
import math


def prime_finder(number):
    prime = [True] * (number + 1)
    for y in range(3, int(math.sqrt(number + 1)), 2):
        if prime[y]:
            prime_list.append(y)
            for x in range(y * y, number + 1, y + y):
                prime[x] = False
    for x in range(y + 2, number + 1, 2):
        if prime[x]:
            prime_list.append(x)


def prime_summation(y):
    for x in prime_list:
        if y + x < 1000000:
            y += x
        else:
            largest_sum.append(y)
            break


def consecutive_prime_sum(number):
    for x in range(-1, -534634, -1):
        if prime_list[x] - number < 0:
            return prime_list[x]


if __name__ == "__main__":
    start = time.time()
    prime_list = [2]
    largest_sum = []
    prime_finder(1000000)
    prime_summation(0)
    print(consecutive_prime_sum(largest_sum[0]))
    end = time.time()
    print(end - start)
