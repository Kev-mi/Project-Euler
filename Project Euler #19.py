import time


def time_checker():
    end = time.time()
    print(end - start)
    exit()


def weekday_counter(start_month, end_month, start_year, end_year,day_value, week_day):
    day_counter = 0
    day_values = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}
    day_value = day_values[day_value]
    for year in range(start_year, end_year+1):
        for month in range(start_month, end_month+1):
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        days = {**dict.fromkeys([1, 3, 5, 7, 8, 10, 12], 31), **dict.fromkeys([4, 6, 9, 11], 30), 2: 29}
                    else:
                        days = {**dict.fromkeys([1, 3, 5, 7, 8, 10, 12], 31), **dict.fromkeys([4, 6, 9, 11], 30), 2: 28}
                else:
                    days = {**dict.fromkeys([1, 3, 5, 7, 8, 10, 12], 31), **dict.fromkeys([4, 6, 9, 11], 30), 2: 29}
            else:
                days = {**dict.fromkeys([1, 3, 5, 7, 8, 10, 12], 31), **dict.fromkeys([4, 6, 9, 11], 30), 2: 28}
            day_value = (day_value + (days[month] % 7)) % 7
            if day_value == day_values[week_day]:
                day_counter += 1
    print("there are " + str(day_counter) + " " + str(week_day) + "s between " + str(start_year) + "-0" + str(start_month) + "-01 and " + str(end_year) + "-" + str(end_month)+"-"+str(days[month]))
    time_checker()


if __name__ == "__main__":
    start = time.time()
    start_month, end_month, star_year, end_year, start_day, week_day = 1, 12, 1901, 2000, "Tuesday", "Sunday"
    weekday_counter(start_month, end_month, star_year, end_year, start_day, week_day)
