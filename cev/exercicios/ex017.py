# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))

# h = (co ** 2 + ca ** 2) ** (1/2)
h = hypot(co, ca)

print(f'O comprimento da hipotenusa mede {h :.2f}')
