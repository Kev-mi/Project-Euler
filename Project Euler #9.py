import time


def pythagorean_triplet(upper_bound):
    for x in range(1, upper_bound):
        for y in range(1, upper_bound):
            z = upper_bound - x - y
            if x**2 + y**2 == z**2:
                return x, y, z


if __name__ == "__main__":
    start = time.time()
    print(pythagorean_triplet(1000))
    end = time.time()
    print(end - start)
