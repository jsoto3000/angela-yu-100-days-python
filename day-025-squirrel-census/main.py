import pandas

data = pandas.read_csv("2018_CP_Squirrel_Census_Data.csv")

fur_color_list = data["Primary Fur Color"].unique()
print(fur_color_list)

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_squirrels_count)
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrels_count)
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
