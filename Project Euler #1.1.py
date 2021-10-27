import time
import math
start = time.time()


def multiples_sum(a, b, upper_bound):
    c = a*b
    a_sum = (math.floor(upper_bound/a) * (a+math.floor(upper_bound/a)*a))/2
    b_sum = (math.floor(upper_bound/b) * (b+math.floor(upper_bound/b)*b))/2
    c_sum = (math.floor(upper_bound/c) * (c+math.floor(upper_bound/c)*c))/2
    return a_sum + b_sum - c_sum


multi_sum = multiples_sum(3, 5, 999)
print(multi_sum)
end = time.time()
print(end - start)
