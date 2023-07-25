cm1 = float(input("Let's determine if three side lengths are a triangle, enter the first in centimeters: "))
cm2 = float(input("Now the second: "))
cm3 = float(input("And the last: "))

if cm1 + cm2 > cm3 and cm2 + cm3 > cm1 and cm1 + cm3 > cm2:
    print("\nThe triangle exists.")

    if cm1 == cm2 and cm1 == cm3:
        print("And it's an \033[1;35mequilateral triangle\033[m.")
    elif cm1 == cm2 or cm1 == cm3 or cm2 == cm3:
        print("And it's an \033[1;36misosceles triangle\033[m.")
    else:
        print("And it's \033[1;36mscalene triangle\033[m.")

else:
    print("\nThe triangle doesn't exist.")
