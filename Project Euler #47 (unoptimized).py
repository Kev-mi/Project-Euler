import time
import math


def prime_checker(number, factor_list_private):
    if number % 2 == 0:
        while number % 2 == 0:
            number = number/2
            factor_list_private.append(2)
    for x in range(3, int(math.sqrt(number))+1, 2):
        if number % x == 0:
            return factor_list_private, number
    if number == 1:
        return factor_list_private, number
    factor_list_private.append(number)
    number = 1
    return factor_list_private, number


def factor_finder(prime_list, factor_list_private, number):
    number_save = number
    for x in prime_list:
        if number % x == 0:
            while number % x == 0:
                number = number / x
                factor_list_private.append(x)
    if number ** 2 > number_save:
        factor_list_private, number = prime_checker(number, factor_list_private)
    return factor_list_private


def prime_finder(number):
    prime_list = [2]
    prime = [True] * (number+1)
    for y in range(3, int(math.sqrt(number+1)), 2):
        if prime[y]:
            prime_list.append(y)
            for x in range(y*y, number + 1, y+y):
                prime[x] = False
    for x in range(y+2, number+1, 2):
        if prime[x]:
            prime_list.append(x)
    return prime_list


def list_product_sum(list):
    product_of_list = 1
    for x in list:
        product_of_list *= x
    return product_of_list


def distinct_primes_factors():
    x = 150000
    prime_list = prime_finder(math.floor(math.sqrt(x + 1)))
    for y in range(3, x, 4):
        y_2, y_3, y_4 = y + 1, y + 2, y + 3
        factor_list = []
        factor_list_2 = []
        factor_list_3 = []
        factor_list_4 = []
        factor_list, y = prime_checker(y, factor_list)
        factor_list = factor_finder(prime_list, factor_list, y)
        if len(set(factor_list)) == 4:
            factor_list_2, y_2 = prime_checker(y_2, factor_list_2)
            factor_list_2 = factor_finder(prime_list, factor_list_2, y_2)
            if len(set(factor_list_2)) == 4:
                factor_list_3, y_3 = prime_checker(y_3, factor_list_3)
                factor_list_3 = factor_finder(prime_list, factor_list_3, y_3)
                if len(set(factor_list_3)) == 4:
                    factor_list_4, y_4 = prime_checker(y_4, factor_list_4)
                    factor_list_4 = factor_finder(prime_list, factor_list_4, y_4)
                    if len(set(factor_list_4)) == 4:
                        y = list_product_sum(factor_list)
                        return y, y + 1, y + 2, y + 3



if __name__ == "__main__":
    start = time.time()
    print(distinct_primes_factors())
    end = time.time()
    print(end - start)
