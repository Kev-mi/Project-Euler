import time


def power_digit_sum(w, z):
    x = list(str(w))
    for y in x:
        z += int(y)
    return z


if __name__ == "__main__":
    start = time.time()
    print(power_digit_sum(2**1000, 0))
    end = time.time()
    print(end - start)
