# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Digite o preço de um produto: R$'))

print(f'O preço desse mesmo produto, mas com 5% de desconto vale R${p - p * 5 / 100 :.2f}')
