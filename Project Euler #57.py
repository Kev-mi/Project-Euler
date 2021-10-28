import time


def square_root_convergents(numerator, denominator):
    count = 0
    for x in range(1, 1001):
        numerator += 2 * denominator
        denominator = numerator - denominator
        if len(str(denominator)) < len(str(numerator)):
            count += 1
    print(count)


if __name__ == "__main__":
    start = time.time()
    square_root_convergents(3, 2)
    end = time.time()
    print(end - start)
