# Desafio 043: Calcular o IMC adaptado.
peso = float(input('Qual o peso? '))
altura = float(input('Qual a altura? '))
IMC = peso / altura**2
print('Seu IMC é de {:.2f}.'.format(IMC), end=" ")
if IMC < 18.5:
    print('Você está abaixo do peso ideal.')
elif 18.5 <= IMC < 25:
    print('Você está no peso ideal.')
elif 25 <= IMC < 30:
    print('Você está com sobrepeso')
elif 30 <= IMC < 40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida')
