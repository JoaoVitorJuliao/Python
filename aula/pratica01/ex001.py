# 1. Faça um programa que dado o valor da temperatura em graus FAHRENHEIT, calcular e escrever o valor da temperatura em graus CELSIUS. Fórmula: C = 5/9 * (F - 32)

c = float(input('Digite uma temperatura em Celsius? '))

print(f'A temperatura {c :.1f}°C, equivale a {c * 9 / 5 + 32 :.1f}°F.')
