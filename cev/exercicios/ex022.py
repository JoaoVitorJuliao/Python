# Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas, o nome com todas minúsculas, quantas letras ao todo (sem considerar espaços) e quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

print(f'O seu nome em maiúsculas é {nome.upper()}.')
print(f'O seu nome em minúsculas é {nome.lower()}.')
print(f'O seu nome tem {len(nome) - nome.count(" ")} letras.')
print(f'O seu primeiro nome tem {nome.find(" ")} letras.')
