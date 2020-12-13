# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno, e tangente desse ângulo.

from math import radians, sin, cos, tan

a = float(input('Digite um ângulo qualquer: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print(f'O ângulo de {a}° tem o Seno {s :.2f}, o Cosseno {c :.2f} e a Tangente {t :.2f}')
