nome = str(input('Digite o seu nome: '))
aprov = []
p = int(input(f'Quantas partidas {nome} jogou? '))
total = 0
for c in range(1,p+1):
    gols = int(input(f'Quantos gols ele fez na partida {c}? '))
    total += gols
    aprov.append(gols)
dic1 = {'Nome':nome,'Aproveitamento':aprov,'Total de gols':total}
print('-='*80)
for a, i in enumerate(aprov):
    print(f'=> Na partida {a+1} ele fez {i} gols. ')
print(f'Foi um total de {total} gols.')
print('-='*80)