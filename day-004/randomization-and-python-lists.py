import random

'''
Randomization

Computers are deterministic.
For pseudo-randomness python uses the Mersenne Twister, 
a general-purpose pseudorandom number generator (PRNG)
Also, see Khan Academy video on PRNGs
Python has a Random module

Module

Split code into modules.

List Data Structure

Use lists to store many data items with orderng capabilities
fruit = [item1, item2]

Also refer to Python documentation on Data Structure (or just use Google)
'''
#random whole number
random_integer = random.randint(1, 10)
print(random_integer)

#random float btween 0 to 1, but not including 1
random_float = random.random()
print(random_float)

#range 0 to 5 but not including 5
random_float = random.random() * 5
print(random_float)

#random love score
love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

#Lists Example

#separate variables for each state is cumbersome
state1 = 'New Jersey'
state2 = 'New York'

#list of all 50 states in alphabetical order
states_of_america = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
                     'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois',
                     'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
                     'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
                     'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
                     'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
                     'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
                     'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

#print first state in above list
#note programmers start count from 0
#offset
print(states_of_america[0])

#print second state in above list
#offset by 1
print(states_of_america[1])

#print second state in above list
#offset by 2
print(states_of_america[2])

#can have both positive and negative indices
#print last state
print(states_of_america[-1])

#print second to last state
print(states_of_america[-2])

#can alter items in list
print(states_of_america[30])
states_of_america[30] = 'New Joisy'
print(states_of_america[30])
states_of_america[30] = 'New Jersey'
print(states_of_america[30])

print(states_of_america[49])

states_of_america.append("Puerto Rico")
print(states_of_america[50])

states_of_america.extend(["Washington, D.C.", "Soto Land"])

print(states_of_america[51])
print(states_of_america[52])



