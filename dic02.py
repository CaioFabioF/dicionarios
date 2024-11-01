import random
import operator
jogo = {'Jogador 1': random.randint(1,6),
        'Jogador 2': random.randint(1,6),
        'Jogador 3': random.randint(1,6),
        'Jogador 4': random.randint(1,6)}
ranking = []
print('Valores sorteados')
print('-='*70)
for k, v in jogo.items() :
    print(f'O {k} tirou {v}')
print('-='*70)
print('RANKING')
ranking = sorted(jogo.items(), key=operator.itemgetter(1),reverse=True)
for i, v in enumerate(ranking) :
    print(f'O {i+1} lugar: {v[0]} tirou o número {v[1]}.')
print('-='*70)