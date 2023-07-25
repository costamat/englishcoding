cm1 = float(input("Let's determine if three side lengths are a triangle, enter the first in centimeters: "))
cm2 = float(input("Now the second: "))
cm3 = float(input("And the last: "))

if cm1 + cm2 > cm3 and cm2 + cm3 > cm1 and cm1 + cm3 > cm2:
    print("The triangle exists.")
else:
    print("The triangle doesn't exist.")
