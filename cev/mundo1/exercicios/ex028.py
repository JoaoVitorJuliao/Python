# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5)

print('-=-' * 20)
print(f'Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('PENSANDO...')
print('-=-' * 20)

sleep(2)

jogador = int(input('Em que número eu pensei? '))

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')
