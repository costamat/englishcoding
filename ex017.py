from math import sqrt

co = float(input("Vamos imaginar um triângulo retângulo, qual o comprimento do cateto oposto em centimetros? "))

ca = float(input("E do cateto adjascente? "))

h = sqrt(co ** 2 + ca ** 2)

print("O triângulo retângulo com cateto oposto de {}cm e cateto adjascente de {}cm possui uma hipotenusa de: {:.2f}cm.".format(co, ca, h))

