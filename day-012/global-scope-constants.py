################### Scope ####################
# For Constants can use global scope variables
# It's not true that you should never use global scope variables

enemies = "Skeleton"

# Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@greatcomix3000"

def increase_enemies():
    enemies = "Zombie"
    return enemies

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
