# Escreva um programa que leia um valor em metros, e o exiba convertido em centímetros e milímetros.

m = float(input('Digite um valor em metro: '))

print(f'Esse valor {m}m, em centímetros vale {m * 100 :.0f}cm e em milímetros vale {m * 1000 :.0f}mm.')
