# Desaafio 042: dizer se é possível formar um triângulo e qual o tipo.
from sys import exit
lado1 = int(input("tamanho do lado 01: "))
lado2 = int(input('Tamanho do lado 02: '))
lado3 = int(input('Tamanho do lado 03: '))
'''if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Com esses seguimentos de retas é possível formar um triângulo ' , end='')
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO')
    elif lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado3 == lado1 != lado2:
        print('ISÓSCELES')
    elif lado1 != lado2 != lado3:
        print('ESCALENO')
        # A construção do escaleno acima só funcionou porque já existia a construção do isóceles.
        # Caso contrário, deveríamos incluir isso ao final da linha: != lado1
else:
    print('Impossível formar um triângulo com esses seguimentos de retas.')'''

# o algorítimo mais limpo e inteligente seria esse abaixo (sugerido pelo professor):
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Com esses seguimentos de retas é possível formar um triângulo ' , end='')
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO')
    elif lado1 != lado2 != lado3 != lado1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('Impossível formar um triângulo com esses seguimentos de retas.')

