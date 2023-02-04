# Desafio 045: criar um jogo "Pedra papel e tesoura"
from time import sleep
from random import choice
print("""Escolha sua opção de jogada de acordo com a lista abaixo:
- pedra
- papel
- tesoura
""")
jogada_user = str(input("Escolha sua jogada: ")).strip()
print('wait...')
sleep(4)
jogada_user = jogada_user.lower()
lista = ['pedra', 'papel', 'tesoura']
jogada_pc = choice(lista)
print(f'Jogada do PC: {jogada_pc}')
if jogada_pc == jogada_user:
    print('Temos um empate')
elif jogada_user == 'pedra' and jogada_pc == 'tesoura' or jogada_user == 'papel' and jogada_pc == 'pedra' or jogada_user == 'tesoura' and jogada_pc == 'papel':
    print('Você ganhou do PC!!!!')
else:
    print('Você perdeu do PC. Sorry!!!')
print('Sua jogada foi {} e a jogada do computador foi {}.'.format(jogada_user, jogada_pc))

