# 4. Faça um programa que leia dois números e mostre qual o maior dos dois. O programa deve informar caso sejam iguais.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'O número {n1} é maior do que o número {n2}.')
elif n1 == n2:
    print('Ambos os números são iguais.')
else:
    print(f'O número {n2} é maior do que o número {n1}.')
