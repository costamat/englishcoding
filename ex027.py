name = str(input("What's your full name? ").title())
name_split = name.split()

print('First name:', name_split[0])
print('Last name:', name_split[len(name_split) - 1])
