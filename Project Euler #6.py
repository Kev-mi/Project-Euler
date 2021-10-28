import time


def sum_square_difference(upper_bound):
    x = sum(x**2 for x in range(1, upper_bound+1))
    return abs((x-(((1+upper_bound)*upper_bound)/2)**2))


if __name__ == "__main__":
    start = time.time()
    print(sum_square_difference(100))
    end = time.time()
    print(end - start)
