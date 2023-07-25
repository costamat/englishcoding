import random

num = random.randint(0, 100)
times = 1

while num <= 90:
    num = random.randint(0, 100)
    times = times + 1

    if num > 90 and times <= 10:
        print('Pronto! Finalmente encontramos um número que serve! o {}.'.format(num))
        print('E só precisamos de {} chances.'.format(times))

    if times >= 11:
        print("""Desculpe, acabaram nossas chances
        Último número: {}
        Tentativas: {}""".format(num, times))
        break

print("Fim...")
