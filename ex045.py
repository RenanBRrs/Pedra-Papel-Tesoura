from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('=-PEDRA=-PAPEL=-TESOURA-=')
print('[0] = PEDRA 💎')
print('[1] = PAPEL 📜')
print('[2] = TESOURA ✂')
jogador = int(input('Digite o valor da sua jogada ===> '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' *13)
print('O computador escolheu: {} '.format(itens[pc]))
print('O jogador escolheu: {} '.format(itens[jogador]))
print('-=' *13)
if pc == 0: #PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador Ganhou')
    elif jogador == 2:
        print('PC ganhou')
    else:
        print('JOGADA INVALIDA')
elif pc == 1: #PAPEL
    if jogador == 0:
        print('PC ganhou')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador Ganhou')
    else:
        print('JOGADA INVALIDA')
elif pc == 2: #TESOURA
    if jogador == 0:
        print('Jogador Ganhou')
    elif jogador == 1:
        print('PC ganhou')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')

