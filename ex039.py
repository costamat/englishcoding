from datetime import date

year = date.today().year

born = int(input("What year were you born? "))

if year - born < 18:
    print("{} years to go until your military enlistment.".format(18 - (year - born)))
elif year - born == 18:
    print("You must enlist this year.")
else:
    print("You are past enlistment season. {} years ago.".format((year - born) - 18))
