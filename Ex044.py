# Desafio 044: formas de pagamento e descontos atrelados a elas
'''print('{:=^40}'.format(' LOJAS TABAJARA '))
preço = float(input('Qual o preço normal do produto? '))
forma_pagamento = str(input("""Formas de pagamento:
[ 1 ] À vista: dinheiro ou cheque - 10% desc.
[ 2 ] À vista: cartão - 5% desc.
[ 3 ] 2X: cartão - preço normal
[ 4 ] 3X ou mais: cartão - 20% de juros
 Escolha uma das opções acima: """))
if forma_pagamento == "1":
    print('O produto terá um desconto de 10% e custará R$ {}{:.2f}'.format('\033[33m', preço * 0.9))
elif forma_pagamento == '2':
    print('O produto terá um desconto de 5% e custará R$ {}{:.2f}'.format('\033[33m', preço * 0.95))
elif forma_pagamento == '3':
    print('O cliente pagará o preço normal do produto: R$ {:.2f}, '.format(preço),end="")
    print('dividido em \033[35mduas parcelas de {:.2f}\033[m'.format(preço / 2))
elif forma_pagamento == '4':
    print('Nesse caso o produto terá um \033[31macréscimo de 20%\033[m e sairá por R$ {:.2f},'.format(preço * 1.20), end="")
    print(' dividido em 3 parcelas de {:.2f}'.format((preço * 1.2) / 3))
elif forma_pagamento != "1" != "2" != "3" != "4":
    print('\033[31mForma de pagamento inválida!')'''
# acima temos o meu código e abaixo temos o código que o professor sugeriu.
print('{:=^40}'.format(' Lojas Tabajara '))
preço_normal = float(input('Qual o valor do produto? '))
print('''Você que pagar de que forma?
[ 1 ] à vista no dinheiro ou cheque, com desconto de 10%
[ 2 ] à vista no cartão, com desconto de 5%
[ 3 ] em 2X no cartão, sem juros (preço normal)
[ 4 ] em 3X ou mais no cartão, com juros de 20%''')
forma_pagamento = str(input('Escolha uma das formas de pagamento acima: '))
if forma_pagamento == "1":
    valor_final = preço_normal * 0.9
elif forma_pagamento == "2":
    valor_final = preço_normal * 0.95
elif forma_pagamento == "3":
    valor_final = preço_normal
    parcela = valor_final / 2
    print("Seu produto será dividido em 2x de {}, sem juros".format(parcela))
elif forma_pagamento == "4":
    valor_final = preço_normal * 1.2
    quantas_parcelas = int(input('Em quantas parcelas você quer dividir? '))
    parcela = valor_final / quantas_parcelas
    print("Seu produto será dividido em {} parcelas de R$ {} e terá o valor final de R$ {}, já com juros de 20%".format(quantas_parcelas, parcela, valor_final))
print('De acordo com sua opção de pagamento, o produto que custava R$ {} sairá por R$ {}.'.format(preço_normal, valor_final))




