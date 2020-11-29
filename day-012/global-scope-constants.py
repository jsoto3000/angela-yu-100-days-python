################### Scope ####################
# Namespaces: Global vs Local Scope
# There is no Block Scope in Python
# Modifying Global Variable

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
