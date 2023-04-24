# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# python slicing lists and tuples

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_tuple[1:])
print(piano_keys[2:5])

# increment
print(piano_keys[::2])

# increment 'trick' to get reversal
print(piano_keys[::-1])
