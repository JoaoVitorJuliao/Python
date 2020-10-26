# 3. Faça um programa para solicitar o nome e as duas notas de um aluno. Calcular sua média e informá-la. Se ela for inferior a 7, escrever "Reprovado”; caso contrário escrever "Aprovado".

n = input('Qual é o nome do(a) aluno(a)? ')
n1 = float(input('Qual foi a primeira nota? '))
n2 = float(input('Qual foi a segunda nota? '))

m = (n1 + n2) / 2

if m < 7:
    print(f'{n}, sua média foi {m :.1f}, inferior a 7, você foi reprovado(a).')
else:
    print(f'{n}, sua média foi {m :.1f}, superior a 7, você foi aprovado(a).')
