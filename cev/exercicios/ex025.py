# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

n = str(input('Digite o seu nome: ')).strip().upper()

nome = n.find('SILVA')

if nome >= 0:
    print('O seu nome tem a palavra Silva.')
else:
    print('O seu nome não tem a palavra Silva.')
