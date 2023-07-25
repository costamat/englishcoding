from datetime import date
year = date.today().year

print("What is your category as an athlete?")
born = int(input('What year were you born? '))

category = year - born

if category < 9:
    print('You are a little athlete.')
elif 9 <= category < 14:
    print('You are a child athlete.')
elif 14 <= category < 19:
    print('You are a junior athlete.')
elif 19 <= category < 20:
    print('You are a senior athlete.')
else:
    print('You are a master athlete.')
