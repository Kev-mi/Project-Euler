import time
import math


def permutationchecker(prime1, prime2, prime3):
    permutationlist = set(list(prime1) + list(prime2) + list(prime3))
    if len(permutationlist) <= 4:
        if int(prime1) != 1487:
            end = time.time()
            print(prime1 + prime2 + prime3)
            print(end - start)
            exit()


def primechecker(number):
    for x in range(3, int(math.sqrt(number + 1)), 2):
        if number % x == 0:
            return False
    return True


def prime_finder(number):
    prime = [True] * (number + 1)
    for y in range(3, int(math.sqrt(number) + 1), 2):
        if prime[y]:
            for x in range(y ** 2, number + 1, y + y):
                prime[x] = False
    for x in range(1001, number + 1, 2):
        if prime[x]:
            prime_list.append(x)


def primesearch():
    for x in prime_list:
        prime = primechecker(x + 3330)
        if prime:
            prime = primechecker(x + 6660)
            if prime:
                permutationchecker(str(x), str(x + 3330), str(x + 6660))


if __name__ == "__main__":
    start = time.time()
    prime_list = []
    prime_finder(10000 - 6660)
    primesearch()
