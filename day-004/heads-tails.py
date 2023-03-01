import random


#Write your code below this line
print("Call it: Heads or Tails!")
heads_tails = input("Enter 'H' for Heads or 'T' for Tails!\n").upper()

if heads_tails == 'H':
    print("You chose Heads. Good Luck!")
else:
    print("You chose Tails. Good Luck!")

print("Coin is flipped!")

random_side = random.randint(0, 1)
if random_side == 1 and heads_tails == "H":
    print("It is Heads. You win!")
elif random_side == 0 and heads_tails == "T":
    print("It is Tails. You win!")
elif random_side == 1 and heads_tails == "T":
    print("It is Heads. Sorry, but you lose!")
elif random_side == 0 and heads_tails == "H":
    print("It is Tails. Sorry, but you lose!")
else:
    print("Holy Cow. The coin landed on its edge.\nTry again!")
