import time
import math


def digit_factorials_3digits(x, upper_bound):
    while int(x) < upper_bound:
        if str(x) == str(int(factorials[int(x[0])]) + int(factorials[int(x[1])]) + int(factorials[int(x[2])])):
            Digit_Factorials.append(int(x))
            x = str(int(x) + 1)
        else:
            x = str(int(x)+1)
        if x[2] == "7":
            x = str(int(x)+3)
        if x[1] == "7":
            x = str(int(x)+30)


def digit_factorials_4digits(x, upper_bound):
    while int(x) < upper_bound:
        if str(x) == str(int(factorials[int(x[0])]) + int(factorials[int(x[1])]) + int(factorials[int(x[2])]) + int(
                factorials[int(x[3])])):
            Digit_Factorials.append(int(x))
            x = str(int(x) + 1)
        else:
            x = str(int(x)+1)
        if x[2] == "8":
            x = str(int(x)+20)
        if x[1] == "8":
            x = str(int(x)+200)
        if x[3] == "8":
            x = str(int(x)+2)


def digit_factorials_5digits(x, upper_bound):
    while int(x) < upper_bound:
        if str(x) == str(int(factorials[int(x[0])]) + int(factorials[int(x[1])]) + int(factorials[int(x[2])]) + int(factorials[int(x[3])])+int(factorials[int(x[4])])):
            Digit_Factorials.append(int(x))
            x = str(int(x) + 1)
        else:
            x = str(int(x)+1)
        if x[3] == "9":
            x = str(int(x)+10)
            if x[2] == "9":
                x = str(int(x)+100)
                if x[1] == "9":
                    x = str(int(x)+1000)


if __name__ == "__main__":
    start = time.time()
    factorials = [math.factorial(x) for x in range(0, 10)]
    Digit_Factorials = []
    digit_factorials_3digits(str(100), 600)
    digit_factorials_4digits(str(1000), 7201)
    digit_factorials_5digits(str(10000), 50000)
    print(sum(Digit_Factorials))
    end = time.time()
    print(end - start)
