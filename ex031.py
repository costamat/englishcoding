km = float(input("What is the distance of the travel in kilometers? "))

if km <= 200:
    print("The ticket will cost: ${:.2f}".format(km * 0.50))
else:
    print("The ticket will cost: ${:.2f}".format(km * 0.45))
