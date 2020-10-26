# 5. Crie um programa que leia a altura de 10 pessoas. Ao final o programa deve informar o total de pessoas cadastradas, a quantidade de pessoas com altura inferior a 1,60 metros; a quantidade de pessoas com altura entre 1,60 metros e 1,80 metros e a quantidade de pessoas com altura superior a 1,80 metros.

alturas = inferior = entre = superior = 0

for altura in range(10):

    altura = float(input(f'Informe a altura: '))

    if altura < 1.6:
        inferior += 1

    elif altura >= 1.6 and altura <= 1.8:
        entre += 1

    else:
        superior += 1

print(f'Foram 10 pessoas cadastradas. {inferior} tem altura inferior a 1.60m, {entre} tem altura entre 1.60m e 1.80m e {superior} tem altura maior que 1.80m.')
