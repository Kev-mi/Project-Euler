import time
import math
start = time.time()
prime_list = [2]


def prime_finder(number):
    prime = [True] * (number+1)
    for y in range(3, int(math.sqrt(number)+1), 2):
        if prime[y] == True:
            prime_list.append(y)
            for x in range(y**2, number + 1, y+y):
                prime[x] = False
    for x in range(y+2, number+1, 2):
        if prime[x] == True:
            prime_list.append(x)


def smallest_multiple(upper_bound):
    lcm = 1
    for x in prime_list:
        y = 1
        while upper_bound > y*x:
            y = y*x
            lcm *= x
    return lcm


user_input = 20
prime_finder(user_input)
answer = smallest_multiple(user_input)
print(answer)

end = time.time()
print(end - start)
