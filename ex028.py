from random import randint

num = randint(0, 5)

aws = int(input('The code chose a number from 0 to 5, which one do you think it is? '))
while aws > 5:
    aws = int(input("Hey! It's from 0 to 5, get right! "))

if aws == num:
    print("Wow! You nailed it, it's {}.".format(aws))
else:
    print("Nop, the chosen number is: {}.".format(num))