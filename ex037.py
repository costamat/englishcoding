num = int(input('Escreva um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para binário.
[ 2 ] Converter para octal.
[ 3 ] Converter para hexadecimal.''')

option = int(input('Sua opção: '))

if option == 1:
    print('{} convertido para BINÁRIO é igual a {}!'.format(num, bin(num)[2:]))
elif option == 2:
    print('{} convertido para OCTAL é igual a {}!'.format(num, oct(num)[2:]))
elif option == 3:
    print('{} convertido para HEXADECIMAL é igual a {}!'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
