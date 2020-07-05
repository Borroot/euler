months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = 1900
day = 0  # monday

count = 0
while year < 2001:
    leap = year % 4 == 0 and year != 1900

    print(year, day)

    for month in months:
        if month == 28 and leap:
            month = 29

        day = (month + day) % 7
        if day == 6 and year > 1900:
            count += 1

    year += 1

print(count)
