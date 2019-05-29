import sys
day, month, year = [int (x) for x in sys.argv[1:]]

if year < 1812 or year > 2019:
    print("Year out of Range")
elif day < 1 or day > 31 or month < 1 or month > 12:
    print("Date not allowed in Calendar") 
else:
    if (year % 400 == 0):
        leap_year = True
    elif (year % 100 == 0):
        leap_year = False
    elif (year % 4 == 0):
        leap_year = True
    else:
        leap_year = False


    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30

    if day > month_length:
        print("Invalid Day in the specified Month") 
    else:
        if day < month_length:
            day += 1
        else:
            day = 1
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
        print("%d-%d-%d" % (day, month, year))