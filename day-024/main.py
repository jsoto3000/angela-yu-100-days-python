# basic open and close file example:

# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# open and close file using 'with' keyword example:

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# write to file example:

# with open("my_file.txt", mode="w") as file:
#     file.write("I was Batman.")

# append to file example:

# with open("my_file.txt", mode="a") as file:
#     file.write("\nI am Batman again.")

# create new file example:

with open("my_new_file.txt", mode="w") as file:
    file.write("I am Robin.")

