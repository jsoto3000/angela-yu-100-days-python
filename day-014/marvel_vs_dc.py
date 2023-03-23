from game_data import marvel_data
from game_data import dc_data
import random
from art import logo, vs
from os_clear import clear

def get_random_marvel_account():
    """Get data from random account"""
    return random.choice(marvel_data)

def get_random_dc_account():
    """Get data from random account"""
    return random.choice(dc_data)

def format_marvel_data(marvel_account):
    """Format account into printable format: name, description and universe"""
    marvel_name = marvel_account["name"]
    marvel_description = marvel_account["description"]
    marvel_universe = marvel_account["universe"]
    # print(f'{marvel_name}: {marvel_account["strength_count"]}')
    return f"{marvel_name}, the {marvel_description}, from the {marvel_universe} universe"

def format_dc_data(dc_account):
    """Format account into printable format: name, description and universe"""
    dc_name = dc_account["name"]
    dc_description = dc_account["description"]
    dc_universe = dc_account["universe"]
    # print(f'{dc_name}: {dc_account["strength_count"]}')
    return f"{dc_name}, the {dc_description}, from the {dc_universe} universe"

def check_answer(guess, marvel_strength_count, dc_strength_count):
    """Checks super powers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if marvel_strength_count > dc_strength_count:
        return guess == "marvel"
    else:
        return guess == "dc"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_marvel = get_random_marvel_account()
    account_dc = get_random_dc_account()

    while game_should_continue:
        account_dc = get_random_dc_account()
        account_marvel = get_random_marvel_account()

        print(f"{format_marvel_data(account_marvel)}!")
        print(vs)
        print(f"{format_dc_data(account_dc)}!\n")

        guess = input("Which universe has the strongest hero? Type 'Marvel' or 'DC': ").lower()

        marvel_strength_count = account_marvel["strength_count"]
        dc_strength_count = account_dc["strength_count"]

        marvel_super_hero = account_marvel["name"]
        dc_super_hero = account_dc["name"]


        if marvel_strength_count == dc_strength_count:
            is_correct = True
        else:
            is_correct = check_answer(guess, marvel_strength_count, dc_strength_count)

        clear()
        print(logo)
        if is_correct and marvel_strength_count == dc_strength_count:
            score += 0
            print(f"It's a tie! You still get to play. Current score: {score}.\n")
            print(f'Marvel\'s {marvel_super_hero} strength level is: {marvel_strength_count}.')
            print(f'DC\'s {dc_super_hero} strength level is: {dc_strength_count}.\n\nPlay again!\n')
        elif is_correct:
            score += 1
            print(f"You win! You get a point. Current score: {score}.\nPlay again!\n")
            print(f'Marvel\'s {marvel_super_hero} strength level is: {marvel_strength_count}.')
            print(f'DC\'s {dc_super_hero} strength level is: {dc_strength_count}.\n\nPlay again!\n')
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Game is terminated. Final score: {score}\n")
            print(f'Marvel\'s {marvel_super_hero} strength level is: {marvel_strength_count}.')
            print(f'DC\'s {dc_super_hero} strength level is: {dc_strength_count}.\n\nGame Over!\n')

game()
