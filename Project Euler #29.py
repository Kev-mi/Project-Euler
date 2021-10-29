import time
terms = []


def distinct_powers(upper_bound):
    for x in range(2, upper_bound+1):
        for y in range(2, upper_bound+1):
            terms.append(x**y)
    return len(set(terms))


if __name__ == "__main__":
    start = time.time()
    print(distinct_powers(100))
    end = time.time()
    print(end - start)
