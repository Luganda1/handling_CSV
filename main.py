# import csv
#
# with open("weather_data.txt", mode="r") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temps = row[1].strip()
#             temps = int(float(temps))
#             temperatures.append(temps)
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.txt")
# # print(data)
# # print(type(data["temp"]))
#
# # data_dict = data.to_dict()
# # print(data_dict)
#
# data_series = data["temp"].to_list
# #
# # # print(type(data_series))
# # data_sum = data["temp"].mean()
# # print(data_sum)
# # largest = data["temp"].max()
# # print(largest)
#
# # row1 = data[data["Day"] == "Monday"]
# #
# # print(row1)
# # max_row = data[data['temp'] == largest]
# # print(max_row)
#
# monday = data[data.Day == "Monday"]
# temp_celcius = monday.temp
#
# temp = temp_celcius*9/5 + 32
#
# print(temp)
#
# #creating dataframe in pandas
# file_name = { "name": ["kamyu", "kamu"]}
# data = pandas.DataFrame(file_name)
# data.to_csv("file_name.csv")

data = pandas.read_csv("squirrel_data.csv")

black = data[data["Primary Fur Color"] == "Black"]
gray = data[data["Primary Fur Color"] == "Gray"]
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
black_col = len(black)
gray_col = len(gray)
cinnamon_col = len(cinnamon)

print(black_col)
print(gray_col)
print(cinnamon_col)
squirrel_color = {
    "color": ["black", "gray", "cinnamon"],
    "squirrel": [black_col, gray_col, cinnamon_col]
}

squirrel_num_col = pandas.DataFrame(squirrel_color)
squirrel_num_col.to_csv("squirrel_number_color.csv")