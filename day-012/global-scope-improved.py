################### Scope ####################
# Namespaces: Global vs Local Scope
# There is no Block Scope in Python
# Modifying Global Variable
enemies = "Skeleton"

def increase_enemies():
    enemies = "Zombie"
    return enemies

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
