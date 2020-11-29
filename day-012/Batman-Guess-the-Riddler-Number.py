from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"Holy Cow Bat Fan! You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'Robin'for an easy level or 'Batman' for a challenging level: ")
    if level == "Batman":
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS

def game():
    print(logo)
    #Choosing a random number between 1 and 100.
    print("Welcome to the Riddler's Guessing Game!")
    print("The Riddler is thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    #Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"Bat Fan, you have {turns} attempts remaining to guess the number.")

        #Let the user guess a number.
        guess = int(input("Make a guess Bat Fan: "))

        #Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses Bat Fan, you lose.")
            return
        elif guess != answer:
            print("Guess again, Bat Fan.")

game()
