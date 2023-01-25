# Desafio 036: condições para aprovar um empréstimo bancário
val_casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o salário? '))
anos = int(input('Em quantos anos a casa será paga? '))
prestação = val_casa / (anos * 12)
if prestação > sal * 0.3:
    print('Seu empréstimo não foi \033[1:31mreprovado')
elif prestação < (sal * 0.3):
    print('Seu empréstimo foi \033[1:31maprovado')
print(f'\033[33mPrestação = {prestação}')
print(f'Margem salarial = {sal * 0.3}')

