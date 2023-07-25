n1 = int(input("Please, enter a number: "))
n2 = int(input("Another: "))
n3 = int(input("And the last: "))

biggest = n1
if n2 > n1 and n2 > n3:
    biggest = n2
if n3 > n1 and n3 > n2:
    biggest = n3
##
smallest = n1
if n2 < n1 and n2 < n3:
    smallest = n2
if n3 < n1 and n3 < n2:
    smallest = n3

print("The biggest number is {}.".format(biggest))
print("The smallest number is {}.".format(smallest))