print("Please, enter two numbers.")

n1 = int(input("The first: "))
n2 = int(input("The second: "))

if n1 > n2:
    print("The first number is the greatest.")
elif n2 > n1:
    print("The second number is the greatest.")
else:
    print("There is no greater number, both are equal.")