# Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A"; Em que posição ela aparece a primeira vez; Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()

print(f"""A letra A aparece {frase.count('A')} vezes na frase.
A primeira letra A apareceu na posição {frase.find('A') + 1}.
A última letra A apareceu na posição {frase.rfind('A') + 1}""")
