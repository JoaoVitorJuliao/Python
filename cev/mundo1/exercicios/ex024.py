# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

c = str(input('Digite o nome de uma cidade: '))

cidade = c.strip().upper()

if cidade[:5] == 'SANTO':
    print('A sua cidade começa com a palavra Santo.')
else:
    print('A sua cidade não começa com a palavra Santo.')
