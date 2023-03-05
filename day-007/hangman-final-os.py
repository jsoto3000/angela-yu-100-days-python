import random
from hangman_art import stages, logo
from hangman_words import word_list
from os_clear import clear

logo()
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print("pssst, here's a hint:", chosen_word[2:])
print("This word has a total of", len(chosen_word), "characters.")

display = []
guessed_letters = []

for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    #Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            print("You guessed right!")
            display[position] = letter
            guessed_letters.append(guess)

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        guessed_letters.append(guess)
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")

    if not "_" in display:
        game_is_finished = True
        print("You win.")
        print(f"The final word is:", ''.join(display))

    print("These are the letters you guessed so far:", guessed_letters)
    print(stages[lives])
