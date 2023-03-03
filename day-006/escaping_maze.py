#lost in maze
#algorithm


#Reeborg's World:
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
#test for edge cases (infinite loop!)
#debugging
#revisit edge cases after day 15
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#edge case: makes sure it has a wall in front
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

'''