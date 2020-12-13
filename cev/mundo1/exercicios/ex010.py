# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1,00 = R$5,74

r = float(input('Quantos reais você tem na carteira? R$'))

print(f'Com R${r} você consegue comprar US${r / 5.74 :.2f}')
