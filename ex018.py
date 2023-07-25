import math
import random

an = random.randint(1, 360)

rad = an * math.pi / 180

sin = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print("The angle {}º has: \n".format(an))
print("sin: {:.2f} \ncos: {:.2f} \ntan: {:.2f}".format(sin, cos, tan))
