'''num = int(input("Please, type a number: "))

num0 = num * 0
num1 = num * 1
num2 = num * 2
num3 = num * 3
num4 = num * 4
num5 = num * 5
num6 = num * 6
num7 = num * 7
num8 = num * 8
num9 = num * 9
num10 = num * 10

print("\n{} Times Table\n".format(num))

print("{} * 0 = {}".format(num, num0))
print("{} * 1 = {}".format(num, num1))
print("{} * 2 = {}".format(num, num2))
print("{} * 3 = {}".format(num, num3))
print("{} * 4 = {}".format(num, num4))
print("{} * 5 = {}".format(num, num5))
print("{} * 6 = {}".format(num, num6))
print("{} * 7 = {}".format(num, num7))
print("{} * 8 = {}".format(num, num8))
print("{} * 9 = {}".format(num, num9))
print("{} * 10 = {}".format(num, num10))
'''
def timestable(plicand):
    plier = int(0)
    table = str('{} * 0 = 0'.format(plicand))
    for number in range(10):
        plier = plier + 1
        table = table + '\n{} * {} = {}'.format(plicand, plier, plicand * plier)
    return table

num = int(input("Please, type a number: "))
print(timestable(num))

