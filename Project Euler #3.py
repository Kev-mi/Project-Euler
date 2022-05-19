import time
import math


def prime_checker(number):
    factor_list = []
    if number % 2 == 0:
        while number % 2 == 0:
            number = number/2
            factor_list.append(2)
    factor_list_2 = []
    for x in range(3, math.floor(math.sqrt(number)+1), 2):
        if number % x == 0:
            while number % x == 0:
                factor_list_2.append(number)
                factor_list.append(x)
                number = number/x
    if len(factor_list_2) == 0:
        factor_list.append(int(number))
        print("prime factors are ", factor_list)
        exit()
    if number == 1:
        print("prime factors are ", factor_list)
        exit()
    return factor_list, number


def factor_finder(prime_list, factor_list, number):
    for x in prime_list:
        if number % x == 0:
            while number % x == 0:
                number = number / x
                factor_list.append(x)
    print("prime factors are ", factor_list)
    return factor_list


def prime_finder(number):
    prime_list = []
    prime = [True] * (number+1)
    for y in range(3, math.floor(math.sqrt(number+1)), 2):
        if prime[y]:
            prime_list.append(y)
            for x in range(y*y, number + 1, y+y):
                prime[x] = False
    for x in range(y+2, number+1, 2):
        if prime[x]:
            prime_list.append(x)
    return prime_list



if __name__ == "__main__":
    start = time.time()
    number = 19
    factor_list, number = prime_checker(number)
    prime_list = prime_finder(math.floor(math.sqrt(number+1)))
    factor_list = factor_finder(prime_list, factor_list, number)
    end = time.time()
    print(end - start)
