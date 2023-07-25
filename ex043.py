print('         BMI Calculator')

height = float(input("What's your height in centimeters? "))
weight = float(input("Enter with your weight in kilograms: "))

height = height / 100
bmi = weight / (height * height)

print('')

if bmi < 16:
    print('Your category is \033[1;31m"Severe thinness"\033[m with {:.1f} kg/m2.'.format(bmi))
elif 16 <= bmi < 18.5:
    print('Your category is \033[1;33m"Thinness"\033[m with {:.1f} kg/m2.'.format(bmi))
elif 18.5 <= bmi < 25:
    print('Your category is \033[1;32m"Normal"\033[m with {:.1f} kg/m2.'.format(bmi))
elif 25 <= bmi < 30:
    print('Your category is \033[1;33m"Overweight"\033[m with {:.1f} kg/m2.'.format(bmi))
elif 30 <= bmi < 40:
    print('Your category is \033[1;31m"Obese"\033[m with {:.1f} kg/m2.'.format(bmi))
else:
    print('Your category is \033[1;31m"Morbid Obesity"\033[m with {:.1f} kg/m2.'.format(bmi))
