# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

l = float(input('Digite em metro, uma largura: '))
a = float(input('Digite em metro, uma altura: '))

area = l * a

print(f'Cada litro de tinta, pinta uma área de 2m². Então para pintar uma parede de {area :.2f}m², você vai precisar de {area / 2 :.0f} litros.')
