################### Scope ####################
# Namespaces: Global vs Local Scope
# There is no Block Scope in Python
# Modifying Global Variable
enemies = "Skeleton"

def increase_enemies():
    global enemies
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
