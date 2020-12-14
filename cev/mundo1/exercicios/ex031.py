# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Qual a distância da sua viagem? '))

print(f'Você está prestes a começar uma viagem de {distancia:.1f}Km.')

preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45  # Maneira simplificada

print(f'E o preço da sua passagem será de R${preco:.2f}')
