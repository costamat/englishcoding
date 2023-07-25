import random

s1 = str(input("Please type the first student name: "))
s2 = str(input("Now the second: "))
s3 = str(input("The third: "))
s4 = str(input("And the fourth: "))

list = [s1.capitalize(), s2.capitalize(), s3.capitalize(), s4.capitalize()]
random.shuffle(list)  # or random.sample(list, k=4)
', '.join(list)

print("The order of students presentation is: {}".format(list))
