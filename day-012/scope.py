################### Scope ####################
# Namespaces: Global vs Local Scope
# There is no Block Scope in Python
# Zombie versus Skeleton

enemies = "Skeleton"

def increase_enemies():
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}")

#Here will output local scope only
increase_enemies()
print(f"enemies outside function: {enemies}")
