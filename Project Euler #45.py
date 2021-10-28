import math
import time


def tri_pen_hex(lower_bound):
    for x in range(lower_bound, 100000000):
        y = x * (2 * x - 1)
        if ((math.sqrt(24 * y + 1) + 1) / 6).is_integer():
            return int(y)


if __name__ == "__main__":
    start = time.time()
    print(tri_pen_hex(286))
    end = time.time()
    print(end - start)
