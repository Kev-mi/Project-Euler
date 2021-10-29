import time
prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]


def totient_maximum(upper_bound):
    summed = 1
    for x in prime_list:
        if summed * x < upper_bound:
            summed *= x
        else:
            return summed


if __name__ == "__main__":
    start = time.time()
    print(totient_maximum(1000000))
    end = time.time()
    print(end - start)
