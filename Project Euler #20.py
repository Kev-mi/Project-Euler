import math
import time


def factorial_digit_sum(upper_bound):
    factorial_sum = 0
    factorial = list(str(math.factorial(upper_bound)))
    for x in factorial:
        factorial_sum += int(x)
    return factorial_sum


if __name__ == "__main__":
    start = time.time()
    print(factorial_digit_sum(100))
    end = time.time()
    print(end - start)
    
