import time


def self_powers(upper_bound):
    sums = []
    for x in range(1, upper_bound+1):
        sums.append(x**x)
    print((str(sum(sums)))[-10:])


if __name__ == "__main__":
    start = time.time()
    self_powers(1000)
    end = time.time()
    print(end - start)
