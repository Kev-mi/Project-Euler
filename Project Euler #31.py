import time


def coin_sums():
    ways = [0] * 201
    ways[0] = 1
    for x in [1, 2, 5, 10, 20, 50, 100, 200]:
        for y in range(x, 201):
            ways[y] += ways[y-x]
    return ways[200]


if __name__ == "__main__":
    start = time.time()
    print(coin_sums())
    end = time.time()
    print(end - start)
