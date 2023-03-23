################### Scope ####################
# Namespaces: Global vs Local Scope
# Global scope does not just apply to variables
# Global scope applies to functions and basically anything else named
# There is no Block Scope in Python (unlike Java)
# If you create a variable within a function it is not available outside function
# But if you create variable within a code block:
# (if, while loop, anything indented with colon) then does not count as creating local scope
# Modifying Global Variable
enemies = "Skeleton"

def increase_enemies():
    # explicitly say have global variable
    # not a best practice to use global scope variables
    # avoid modifying global variable within function
    global enemies
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
