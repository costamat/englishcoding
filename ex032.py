year = int(input("Find out if your year is a leap year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("{} is a leap year.".format(year))
else:
    print("{} isn't a leap year.".format(year))
