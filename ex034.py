salary = float(input("You can get a raise. What is your salary? "))

if salary > 1250:
    print("Your increased salary is: {}".format(salary * 0.10 + salary))
else:
    print("Your increased salary is: {}".format(salary * 0.15 + salary))
