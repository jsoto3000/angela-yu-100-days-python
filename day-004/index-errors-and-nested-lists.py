'''
Index Errors
Try to fetch something beyond list size
'''

#list of all 50 states in alphabetical order
states_of_america = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
                     'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois',
                     'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
                     'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
                     'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
                     'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
                     'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
                     'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

num_states = len(states_of_america)
print("Number of States =", num_states, "\n")
#subtracting 1 avoids index error out of range
print("The last alphabetical state is", states_of_america[num_states-1], "\n")


#dirty_dozen fruits/vegetables lists
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes",
               "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

print(dirty_dozen,"\n")

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen,"\n")
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[0][2])
print(dirty_dozen[0][3])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])


