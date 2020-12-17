# Number Manipulations and F Strings

# Rounding

a = (8/3)
print(int(a))
print(type(a))

b = (8/3)
print(round(b))
print(type(b))

c = (8/3)
print(round(c, 2))
print(type(c))

# Floor Division

d = (8//3)
print(d)
print(type(d))

# Continuing calculations on variable

result = 4/2
print("result =", result)
result /= 2
print("result now =", result)

# Keeping track of scores example

# User starts with zero score
score = 0
# User scores one point
score += 1
print("User\'s current score is", score)

score += 1
print("User\'s current score is", score)

score -= 1
print("User\'s current score is", score)

print(f"User\'s current score is {score}")

score = 1
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, and it is {isWinning} that you are winning.")
