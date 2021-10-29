import time
import math

divisor_sums = []
amicable = []


def divisors_generator(upper_bound):
    for x in range(1, upper_bound):
        divisor_list = []
        for y in range(1, int(math.sqrt(x) + 1)):
            if x % y == 0:
                divisor_list.append(int(x / y))
                divisor_list.append(y)
        if (sum(divisor_list) - x) < 10001:
            divisor_sums.append(sum(divisor_list) - x)
        else:
            divisor_sums.append(0)


def amicable_numbers(upper_bound):
    for x in range(1, upper_bound):
        y = divisor_sums[x - 1]
        if x != y:
            z = divisor_sums[y - 1]
            if z == x:
                amicable.append(x)
    return sum(amicable)


if __name__ == "__main__":
    start = time.time()
    divisors_generator(10001)
    print(amicable_numbers(10000))
    end = time.time()
    print(end - start)
