days = int(input("How many rented days? "))
km = float(input("And how many kilometers traveled? "))

rent = (days * 60) + (km * 0.15)

print("The total amount you will pay is R${:.2f}".format(rent))
