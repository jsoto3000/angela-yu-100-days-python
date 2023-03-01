#Write your code below this row 👇

# range(start, stop, step)

sum = 0
# 1 - 101, but 101 excluded so really 1 to 100
for number in range(1, 101):
  # print(number)
    sum += number
    print(sum)
print(sum)

#or

alternative_sum = 0
#1 - 101, but 101 excluded so really 1 to 100
for number in range(1, 101):
    if number % 2 == 0:
    # print(number)
        alternative_sum += number
print(alternative_sum)

even_sum = 0
# 2 - 101, but 101 excluded so really 2 to 100
for number in range(2, 101, 2):
  # print(number)
    even_sum += number
print(even_sum)

#or

alternative_sum = 0
#1 - 101, but 101 excluded so really 1 to 100
for number in range(1, 101):
    if number % 2 == 0:
    # print(number)
        alternative_sum += number
print(alternative_sum)
