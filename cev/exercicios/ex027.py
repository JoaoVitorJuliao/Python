# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. Ex: Ana Maria de Souza; primeiro = Ana; último = Souza

nome = str(input('Digite o seu nome completo: ')).strip().split()

print(f"""Muito prazer em te conhecer!
O seu primeiro nome é {nome[0]}
O seu último nome é {nome[len(nome) - 1]}""")
