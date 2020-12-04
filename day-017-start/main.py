# PascalCase for classes
# camelCase not used
# snake_case everything else

# attributes - information, qualities, properties
# method - function attached to an object


class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        # print("new user being created")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "javier")
user_2 = User("002", "rosie")
# user_1.id = "001"
# user_1.username = "javier"

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# Constructor
# class Car
#   def__init__(self, seats):
#       self.seats = seats
#   initialize attributes
# my_car = Car(5)




