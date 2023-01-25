# Desafio 039: alistamento militar de acordo com o ano de nascimento
ano_nasc = int(input('Qual o seu ano de nascimento? '))
from datetime import date
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

