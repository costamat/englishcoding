km = float(input("How many kilometers per hour was this car driving? "))

if km > 80:
    print("The car has exceeded the speed limit! (80 km/h)")
    print("The traffic fine will cost $ {:.2f}.\n$ 7.00 per km exceeded.".format((km - 80) * 7))
else:
    print("All right!")
