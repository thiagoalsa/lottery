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
        util.print_red('Error Enter between 6 and 15')


# CALCULATION OF THE VALUE OF EACH BET

list_of_values = {'6': 4.5, '7': 31.5, '8': 126, '9': 378, '10': 945, '11': 2079, '12': 4158, '13': 7722,
                 '14': 13513.5, '15': 22522.5}
value_bet = list_of_values[f'{quantity_of_numbers}']
print('-' * 40)
print(f'The value of each bet will be -> ', util.cambio(value_bet))
sleep(0.5)
print('-' * 40)
print(f'Select {quantity_of_numbers} numbers from 1-60. ')
print('-' * 40)
sleep(0.5)

# COLLECTING PLAYER NUMBERS

chosen_numbers = []

while len(chosen_numbers) != int(quantity_of_numbers):
    choice = int(input('Choose a number between 1 and 60: '))
    if choice in chosen_numbers:
        util.print_red('Error you already chose that number.')
    elif choice > 60:
        util.print_red('Error Choose only between 1 and 60.')
    elif choice < 1:
        util.print_red('Error Choose only between 1 and 60.')
    else:
        chosen_numbers.append(choice)
        print(f'Chosen numbers -> {chosen_numbers}')
        print(f'You already chose {len(chosen_numbers)} of {quantity_of_numbers}.')
        print('-' * 40)

# DRAW THE NUMBERS

print(f' Your chosen numbers were {sorted(chosen_numbers)}')
chosen_numbers = sorted(chosen_numbers)
sleep(1)

# COUNTERS

counter = 0
sena = 0
quina = 0
quadra = 0

# CHECKING THE NUMBERS

while True:

    raffle = util.raffle(6, 60)
    counter += 1
    print(f'{counter}º - {raffle}')

    match = util.match_number(raffle, chosen_numbers)

    if util.total_match_number(match) == 6:
        util.print_green(f"You won in SENA with {counter} attempts.")
        sena += 1
        break
    elif util.total_match_number(match) == 5:
        quina += 1

    elif util.total_match_number(match) == 4:
        quadra += 1

    elif counter == 1000000:
        break


print(f'        FINISH!      ')
print('-' * 50)
print(f'You won {sena} time in SENA.')
print('-' * 50)
print(f'You won {quina} times in QUINA.')
print('-' * 50)
print(f'You won {quadra} times in QUADRA.')
print('-' * 50)
print(f'The total cost of the bets was', util.cambio(counter * value_bet))
print('-' * 50)
print(f"it's been about {counter / 104:.0f} years.")

