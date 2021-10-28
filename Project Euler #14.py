import time


def longest_collatz_sequence(upper_bound):
    chain, record = 0, 0
    numbers = {}
    for x in range(3, upper_bound, 2):
        y = x
        if chain > record:
            record2, record = y-2, chain
        chain = 0
        while x > 1:
            if x % 2 == 0:
                x /= 2
                chain += 1
            else:
                if x in numbers:
                    chain += numbers[x]
                    break
                x = (3*x+1)/2
                chain += 2
        numbers[y] = chain
    print(record2)


if __name__ == "__main__":
    start = time.time()
    longest_collatz_sequence(1000000)
    end = time.time()
    print(end - start)
