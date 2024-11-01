n = str(input('Digite o seu nome: '))
m = int(input('Digite a média: '))
s = m
dados = {'Nome':n,'Média':m,'Situação': 0}
if m > 70 and m <= 100 :
    dados['Situação'] = 'Aprovado'
elif m < 70 and m > 60 :
    dados['Situação'] = 'Recuperação'
else :
    dados['Situação'] = 'Reprovado'  
for k, v in dados.items():
    print(f'{k} é igual a {v}')