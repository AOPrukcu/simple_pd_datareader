#with open("weather_data.csv") as data_file :
#    data = data_file.readlines()
#data.
#print(data)

#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")


# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# temp_average = data["temp"].mean()
# print(temp_average)
#
# print(data["temp"].max())

# print(data[data["temp"] == data["temp"].max()])

# monday = data[data.day=="Monday"]
# monday_temp = monday["temp"]
# monday_temp_f = monday_temp*1.8+32
# print(monday_temp_f)

# data_dict = {
#     "students": ["amy","james","angela"],
#     "scores":[76,56,65]
# }
# data = pd.DataFrame(data_dict)
# data.to_csv("new_Data.csv")
# print(data)

squirrels = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(squirrels[squirrels["Primary Fur Color"]=="Gray"])
red = len(squirrels[squirrels["Primary Fur Color"]=="Cinnamon"])
black = len(squirrels[squirrels["Primary Fur Color"]=="Black"])

squirrel_count_dic = {"fur color" :["gray","red","black"],
                  "count": [gray,red,black]
                  }
squirrel_count = pd.DataFrame(squirrel_count_dic)
print(squirrel_count)

squirrel_count.to_csv("squirrel_counts")



