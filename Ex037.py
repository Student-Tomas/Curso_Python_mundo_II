# Desafio 037: converção de números para binário, octal e hexadecimal
num = int(input('Diga um número: '))
print('''Escolha uma das opções de conversão abaixo:
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opção = int(input('Sua escolha: '))
if opção == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexagonal é {}'.format(num, hex(num)[2:]))
else:
    print('Você escolheu uma opção inválida')

