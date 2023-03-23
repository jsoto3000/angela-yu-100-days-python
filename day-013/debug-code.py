############DEBUGGING######################

#1 - Describe the Problem
#2 - Reproduce the bug
#3 - PLay computer
#4 - Fix the errors
#5 - Print is your friend
#6 - Use a debugger
#7 - Take a break
#8 - Ask a friend
#9 - Run code often
#10 - Search/Ask stackoverflow.com

# 1 - Describe Problem
# def my_function():
#   for i in range(1, 20):
# never reaches 20, range should be 1, 21
#     if i == 20:
#       print("You got it")
# my_function()


# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# range for index should be 0, 5
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
# should be >= 1994
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# input should be int
# if age > 18:
# print("You can drive at age {age}.")
# print should be indented

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# "==" is not assignment, checks for equality
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger: pythontutor.com
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   use breakpoint with Debugger
#   append happens outside of loop, correct by indenting line code
#   print(b_list)

# mutate([1,2,3,5,8,13])

# Run Code often to debug
# Search StackOverFlow.com for errors
