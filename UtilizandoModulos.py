from math import sqrt, floor, ceil
import emoji

num = int(input("Type a number: "))

# root = math.sqrt(num)
root = sqrt(num)

print("The square root of {} is {}.".format(num, floor(root)))

print(emoji.emojize("Hello world!!! :earth_americas: :snowman: :umbrella:", use_aliases=True))