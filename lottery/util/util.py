import random


def raffle(number_of_numbers: int, game_size: int):
    """
    Draws a desired amount of numbers in descending order.

    Args:
        number_of_numbers: number of numbers that will be randomly drawn.
        game_size: the highest number that can be drawn

    Returns:
         different numbers in descending order
    """
    numbers_drawn = random.sample(range(1, game_size + 1), number_of_numbers)
    return sorted(numbers_drawn)


def match_number(numbers_drawn: list, numbers_chosen: list):
    """
    Create a list with the numbers that two other lists have in common.

    Args:
        numbers_drawn: a list of drawn numbers
        numbers_chosen: a list of chosen numbers
    Returns:
        a list of numbers that numbers_drawn and numbers_chosen have in common.
    """
    list_match = []
    for number in numbers_drawn:
        if number in numbers_chosen:
            list_match.append(number)
    return list_match


def total_match_number(match_num: list):
    return len(match_num)


def cambio(price: int, cambio='R$'):
    return f'{cambio}{price:_.2f}'.replace('.', ',').replace('_', '.')


def print_red(txt: str):
    red = f'\033[41m{txt}\033[m'
    print(red)

def print_green(txt: str):
    green = f'\033[42m{txt}\033[m'
    print(green)

