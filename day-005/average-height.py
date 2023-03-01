# Don't change the code below
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)
# Don't change the code above
# Do not use sum() and len() functions

#Write your code below this row

total_height = 0
for height in student_heights:
    total_height += height
print(f"the summed heights = {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"the average height =", average_height)
