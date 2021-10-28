import math
import time


def highly_divisible_triangular_number(number):
    factors = [1]
    for x in range(2, int(math.sqrt(number)+1)):
        if number % x == 0:
            factors.append(number/x)
            factors.append(x)
    if len(factors) > 500:
        answer.append(number)
        print(number)


def triangle_number_generator(lower_bound, upper_bound):
    for x in range(lower_bound, upper_bound):
        if len(answer) == 1:
            break
        highly_divisible_triangular_number((x*(x+1))/2)


def lower_bound_finder(summation):
    triangle_number_generator(int(((math.sqrt(8*summation+1)-1)/2)), 34673462)


if __name__ == "__main__":
    start = time.time()
    answer = []
    lower_bound_finder((2**4)*(3**4)*(5**4)*(7*11))
    end = time.time()
    print(end - start)
