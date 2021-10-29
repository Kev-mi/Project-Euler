import time


def number_letter_counts1(sums):
    for x in range(21, 100):
        char = str(x)
        sums += two_digits[int(char[0])]
        sums += one_digit[int(char[1])]
    two_digit_sums.append(sums)


def number_letter_counts2(sums):
    for x in range(100, 1000):
        char = str(x)
        sums += one_digit[int(char[0])] + 7
        sums += two_digits[int(char[1])]
        sums += one_digit[int(char[2])]
    three_digit_sums.append(sums)

if __name__ == "__main__":
    start = time.time()
    one_digit = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
    two_digits_end = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    two_digits = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
    two_digit_sums = []
    three_digit_sums = []
    a = sum(one_digit)
    b = sum(two_digits_end)
    number_letter_counts1(a + b + 6)
    number_letter_counts2(0)
    print(sum(two_digit_sums) + sum(three_digit_sums) + len("onethousand") + (99 * 9 * 3) + (4 * 9))
    end = time.time()
    print(end - start)
