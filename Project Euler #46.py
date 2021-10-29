import time
import math


def prime_finder(number):
    prime = [True] * (number + 1)
    for y in range(3, int(math.sqrt(number + 1)), 2):
        if prime[y]:
            for x in range(y * y, number + 1, y + y):
                prime[x] = False
    for x in range(3, number + 1, 2):
        if prime[x]:
            prime_list.append(x)
        else:
            odd_composites.append(x)


def goldbachs_other_conjecture():
    for x in odd_composites:
        for y in prime_list:
            if x > y:
                if not math.sqrt((x - y) / 2).is_integer():
                    continue
                else:
                    break
            else:
                return x


if __name__ == "__main__":
    start = time.time()
    prime_list = [2]
    odd_composites = []
    prime_finder(6000)
    print(goldbachs_other_conjecture())
    end = time.time()
    print(end - start)
