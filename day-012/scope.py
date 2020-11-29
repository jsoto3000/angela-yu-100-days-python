################### Scope ####################
# Namespaces: Global vs Local Scope
# There is no Block Scope in Python
enemies = "Skeleton"

def increase_enemies():
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
