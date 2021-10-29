import math
import time


def pentagon_number_generator():
    for x in range(1, 5000):
        pentagon_numbers.append(int((x * (3 * x - 1)) / 2))


def finder():
    for x in pentagon_numbers:
        for y in pentagon_numbers:
            if x > y:
                if ((math.sqrt(24*(x+y)+1)+1)/6).is_integer():
                    if ((math.sqrt(24*(x-y)+1)+1)/6).is_integer():
                        end = time.time()
                        print(end - start)
                        return abs(x-y)
                    else:
                        break
            else:
                break


start = time.time()
pentagon_numbers = []
pentagon_number_generator()
finder()
print(pentagon_numbers)
