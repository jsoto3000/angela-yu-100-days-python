import csv
import pandas

# with open("weather_data.csv") as data_file:
#     # readlines method (note there is also a readline method)
#     data = csv.reader(data_file)
#     # csv.reader object can be looped thru to get data
#     temperatures = []
#     for row in data:
#         print(row)

# with open("weather_data.csv") as data_file:
#     # readlines method (note there is also a readline method)
#     data = csv.reader(data_file)
#     # csv.reader object can be looped thru to get data
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# print(data["temp"].mean())
#
# print(data["temp"].max())

# get data in row

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# create a data frame from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv("new_data.csv")
