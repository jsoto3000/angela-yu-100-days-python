# Python Functions
# Way to bundle instructions

print("Hello")

num_char = len("Hello")
print(num_char)

# Defining Functions
'''
def my_function():
    Do this
    Then do this
    Finally do this


def my_function():
    print("Hello")
    print("Bye")

#call my_function
my_function()

# Karel the robot


Reeborg's World: 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

#make robot draw square

turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

#hurdles loop challenge

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#instead of writing jump() six time
#use for loop

for step in range(6):
    jump()

#while loop example

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -=1
    print(number_of_hurdles)    

#hurdles loop challenge number two

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True:
    jump()

#Version 1 not equal to True 
#False until reaches goal  
while at_goal() != True:
    jump()

#Version 2 negation
#False until reaches goal
while not at_goal():
    jump()

#Hurdles Challenge using While loops

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front:
        jump()
    else:
        move()
        
#Jumping over Hurdles with Variable Heights

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while_wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front:
        jump()
    else:
        move()

'''