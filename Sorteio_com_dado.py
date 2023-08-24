from random import randint
from operator import itemgetter
from time import sleep
lista = {'jogador1': randint(1, 6),     # Lista inicial dos números sorteados
     'jogador2': randint(1,6),
     'jogador3': randint(1,6),
     'jogador4': randint(1,6)}
ranking = list()
sleep(1)

for letra in 'sorteando valores...':
    print(letra,end='')
    sleep(0.25)
print()
sleep(2)
print('-='*30)

for k, v in lista.items():      #   Apresentação dos valores tabulados
    print(f'{k} tirou {v} no dado.')
print('-='* 30)

for letra in 'Organizando valores...':
    print(letra,end='')
    sleep(0.15)
print()
sleep(2)

ranking = sorted(lista.items(), key=itemgetter(1), reverse=True)     # Apresentação do ranking dos numeros sorteados
for k, v in enumerate(ranking):
    print(f'Em {k+1}° lugar ficou o {v[0]} com {v[1]} no dado.')
sleep(2)
print(19 * '*','FIM', 19 * '*')
