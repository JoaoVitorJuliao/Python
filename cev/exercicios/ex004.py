# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ')

print(f'''
O tipo primitivo desse valor é {type(a)}
Só tem espaços? {a.isspace()}
É um número? {a.isnumeric()}
É alfabético? {a.isalpha()}
É alfanumérico? {a.isalnum()}
Está em maiúsculas? {a.isupper()}
Está em minúsculas? {a.islower()}
Está capitulada? {a.istitle()}
''')
