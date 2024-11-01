import datetime
nome = str(input('Digite o seu nome: '))
anon = int(input('Digite o seu ano de nascimento: '))
carteirat = int(input('Digite o número da sua carteira de trabalho: '))

dic1 = {'nome':nome,'ano de nascimento':anon,'carteira de trabalho':carteirat}
if carteirat != 0 :
    dic1['ano de contratação'] = int(input('Digite o seu ano de contratação: '))
    dic1['salario'] = int(input('Digite o seu salário: '))
    d = datetime.datetime.now().year - anon
    apos = 65 - d
    dic1['aposentadoria'] = apos
for k, v in dic1.items() :
    print(f'{k} tem o valor {v}')