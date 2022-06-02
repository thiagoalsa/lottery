import random
from time import sleep
from util import util

# QUANTITY OF BET NUMBERS

while True:
    quantity_of_numbers = int(input('How many numbers do you want to bet? [min: 6 , max: 15]?  '))
    if 5 < quantity_of_numbers < 16:
        quantity_of_numbers = str(quantity_of_numbers)
        break
    else:
        print_red


# CALCULO DO VALOR DE CADA APOSTA

lista_valores = {'6': 4.5, '7': 31.5, '8': 126, '9': 378, '10': 945, '11': 2079, '12': 4158, '13': 7722,
                 '14': 13513.5, '15': 22522.5}
valor_aposta = lista_valores[f'{quantity_of_numbers}']
print('-' * 40)
print(f'O valor de cada aposta sera de', util.cambio(valor_aposta))
sleep(3)
print('-' * 40)
print(f'Select {quantity_of_numbers} numbers from 1-59. ')
print('-' * 40)
sleep(0.5)

# COLETANDO OS NUMEROS DO JOGADOR

numeros_escolhidos = []
while len(numeros_escolhidos) != int(quantity_of_numbers):
    escolha = int(input('Escolha um numero entre 1 e 60: '))
    if escolha in numeros_escolhidos:
        print('Erro voce ja escolheu esse numero.')
    elif escolha > 60:
        print('Erro! Escolha apenas entre 1 e 60')
    elif escolha < 1:
        print('Erro! Escolha apenas entre 1 e 60')
    else:
        numeros_escolhidos.append(escolha)
        print(f'Numeros escolhidos -> {numeros_escolhidos}')
        print(f'Voce já escolheu {len(numeros_escolhidos)} de {quantity_of_numbers}.')
        print('-' * 40)

# SORTEANDO OS NUMEROS

print(f' Seus numeros escolhidos foram {sorted(numeros_escolhidos)}')
numeros_escolhidos = sorted(numeros_escolhidos)
sleep(3)
contador = 0
sena = 0
quina = 0
quadra = 0

# CONFERINDO OS NUMEROS

while True:
    sorteio = util.raffle(6, 59)
    contador += 1
    print(f'{contador}º - {sorteio}')

    match = util.match_number(sorteio, numeros_escolhidos)

    if util.total_match_number(match) == 6:
        print_green(f"Voce venceu na Sena com {contador} tentativas.")
        sena += 1
        break
    elif util.total_match_number(match) == 5:
        quina += 1

    elif util.total_match_number(match) == 4:
        quadra += 1

    elif contador == 1000000:
        break


print(f'        ACABOU!      ')
print('-' * 50)
print(f'Voce ganhou {sena} vez na SENA')
print('-' * 50)
print(f'Voce ganhou {quina} vezes na QUINA.')
print('-' * 50)
print(f'Voce ganhou {quadra} vezes na QUADRA.')
print('-' * 50)
print(f'O custo total das apostas foi de', util.cambio(contador * valor_aposta))
