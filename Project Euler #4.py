import time
start = time.time()
palindrome = []


def maxi(upper_bound):
    for x in range(100, upper_bound):
        for y in range(100, x):
            if str(x*y) == str(x*y)[::-1]:
                palindrome.append(x*y)


maxi(1000)
print(max(palindrome))
end = time.time()
print(end - start)

