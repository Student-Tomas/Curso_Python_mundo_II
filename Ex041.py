# Desafio 041: saber a categoria do nadador de acordo com a idade
from datetime import date
nascimento = int(input('Ano de nascimento do atleta: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
if idade > 25:
    print('O atleta está na categoria MASTER')
elif 19 < idade <= 25:
    print('O atleta está na categoria SÊNIOR')
elif 14 < idade <= 19:
    print('O atleta está na categoria JÚNIOR')
elif 9 < idade <= 14:
    print('O atleta está na categoria INFANTIL')
else:
    print('O atleta está na categoria MIRIM')
