from itertools import permutations
import time


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def digit_permutations(n):
    digits = [int(d) for d in str(n)]
    for perm in permutations(digits):
        yield int(''.join(str(d) for d in perm))


def permutation_iterator(number):
    for p in digit_permutations(number):
        prime = is_prime(p)
        if prime:
            prime_list.append(p)
    return prime_list


if __name__ == "__main__":
    start = time.time()
    prime_list = []
    number = 1234567
    prime_list = permutation_iterator(number)
    print(max(prime_list))
    end = time.time()
    print(end - start)
