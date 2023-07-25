from random import choice

s1 = str(input("Please type the first student name: "))
s2 = str(input("Now the second: "))
s3 = str(input("The third: "))
s4 = str(input("And the fourth: "))

list = [s1, s2, s3, s4]

choice = choice(list)

print("\n {} \n {} \n {} \n {} \n".format(s1, s2, s3, s4))

print("The chosen student is: " + choice)
