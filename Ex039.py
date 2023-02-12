# Desafio 039: alistamento militar de acordo com o ano de nascimento
from sys import exit
from datetime import date
sexo = str(input('''Escolha uma das opções de sexo abaixo:  
[ M ] para MULHER
[ H ] para HOMEM
Resp: '''))
if sexo.upper() == "M":
    print('Você não precisar se alistar')
    exit()
elif sexo.upper() == "H":
    print('Responda a questão abaixo:')
else:
    print('Opção inválida')
    exit()
ano_nasc = (input('Qual o seu ano de nascimento? '))
if ano_nasc.isdigit() and len(ano_nasc) == 4:
    ano_nasc = int(ano_nasc)
    ano_atual = date.today().year
    alistamento = ano_nasc + 18
    dif_a_menos = alistamento - ano_atual
    dif_a_mais = ano_atual - alistamento
    if alistamento - 1 > ano_atual:
        print('Você vai se alistar em {}. Ainda faltam {} anos.'.format(alistamento, dif_a_menos))
    elif dif_a_menos == 1:
            print('Você vai se alistar em {}. Ainda falta {} ano.'.format(alistamento, dif_a_menos))
    elif ano_atual > alistamento + 1:
        print('Você deveria ter se alistado em {}. Já se passaram {} anos.'.format(alistamento, dif_a_mais))
    elif dif_a_mais == 1:
        print('Você deveria ter se alistado em {}. Já se passou {} ano'.format(alistamento, dif_a_mais))
    else:
        print('{} é o seu ano de alistamento. Apresente-se a uma junta militar logo!'.format(ano_atual))
else:
    print('You have to enter a four digits valid year')
