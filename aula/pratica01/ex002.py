# 2. Elabore um programa para solicitar o nome de uma equipe de futebol, a quantidade de derrotas, empates e vitórias obtidas por ela no campeonato. No futebol, cada vitória vale três pontos e cada empate vale um ponto. Calcular e informar: a quantidade de pontos ganhos, a quantidade de pontos perdidos e o percentual de aproveitamento da equipe.

nome = input('Digite o nome da equipe: ')
der = int(input('Quantas derrotas a equipe teve? '))
emp  = int(input('Quantos empates a equipe teve? '))
vit = int(input('Quantas vitórias a equipe teve? '))

tot = der + emp + vit
pm = tot * 3
pv = vit * 3
pg = pv + emp
pp = pm - pg
prct = int(pg / pm * 100)

print(f'A equipe ganhou {pg} pontos, perdeu {pp} pontos e seu aproveitamento é de {prct}%.')
