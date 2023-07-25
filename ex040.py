print("=-=" * 20)
print("Average Calculator")
print("=-=" * 20, "\n")

r1 = float(input("Please, type the first test result: "))
r2 = float(input("Now the second: "))

ats = (r1 + r2) / 2

print('')

if ats < 5:
    print("The average test score is: {}\n\033[31mYou are flunked!".format(ats))
elif 5 <= ats < 7:
    print("The average test score is: {}\n\033[33mYou will need to recover!".format(ats))
else:
    print("The average test score is: {}\n\033[32mYou are approved!".format(ats))
