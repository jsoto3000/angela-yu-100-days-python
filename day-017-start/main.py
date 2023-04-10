# Intro to Constructors

# Constructor
# class Car
#   def__init__(self, seats):
#       self.seats = seats
#   initialize attributes
# my_car = Car(5)

class User:
    """Blueprint for User Object containing its attributes and methods"""
    # initialize attributes
    def __init__(self, user_id, username):
        # attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        # print("new user being created")

    #method
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "joe")
user_2 = User("002", "susan")

# user 1 'Joe' follows user 2 but has no followers
user_1.follow(user_2)
print("User Name is:", user_1.username)
print("Number of followers =", user_1.followers)
print("Number of users following =", user_1.following, "\n")

# user 2 'Susan' is followed by user 1 'Joe' but follows no one
print("User Name is:", user_2.username)
print("Number of followers =", user_2.followers)
print("Number of users following =", user_2.following)






