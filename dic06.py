galera = list()
pessoa = dict()
soma = media = 0
while True :
    pessoa.clear()
    pessoa['Nome'] = str(input('Digite o seu nome: '))
    while True:
        pessoa['Sexo'] = str(input('Digite o seu sexo[F/M]: ')).strip().upper()
        if pessoa['Sexo'] not in 'FfMm' :
            print('ERRO! Digite novamente. ')
        else :
            break
    pessoa['Idade'] = int(input('Digite a sua idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True :
        continuar = str(input('Deseja continuar[S/N]? ')).strip().upper()
        if continuar not in 'SsNn' :
            print('ERRO! Digite apenas S ou N. ')
        if continuar in 'SsNn' :
            break
    if continuar in 'Nn' :
        break
media = soma / len(galera)
print('-='*70)
print(f'Ao todo temos {len(galera)} pessoas')
print('-='*70)
print(f'A média de idade é {media:5.2f}')
print('-='*70)
print('Mulheres cadastradas:')
for p in galera :
    if p['Sexo'] in 'Ff':
        print(f'{p['Nome']}',end='')
print('-='*70)
for p in galera:
    if p['Idade'] >= media :
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v} ',end='')
        print()
print('-='*70)
print('FIM.')