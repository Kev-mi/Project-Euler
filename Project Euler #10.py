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
    return sum(prime_list)


if __name__ == "__main__":
    prime_list = [2]
    start = time.time()
    print(prime_finder(1999999))
    end = time.time()
    print(end - start)
