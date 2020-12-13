# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite um salário: R$'))

print(f'O mesmo salário, mas com aumento de 15% aplicado, vale R${s + s * 15 / 100 :.2f}')
