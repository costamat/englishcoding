""""number = '000' + str(input("Please, insert a number from 0 to 9999: "))
qt = len(number)

print("Units:", number[qt - 1])
print("Tens:", number[qt - 2])
print("Hundreds:", number[qt - 3])
print("Thousands:", number[qt - 4])"""

numreal = str(input("Please, insert a number from 0 to 9999: "))
num_zeros = '000' + numreal
qt = len(num_zeros)

print("Units:", num_zeros[qt - 1])
print("Tens:", num_zeros[qt - 2])
print("Hundreds:", num_zeros[qt - 3])
print("Thousands:", num_zeros[qt - 4])
