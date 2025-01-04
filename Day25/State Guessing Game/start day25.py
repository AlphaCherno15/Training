import csv
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = data["Primary Fur Color"]
gray = len(data[color == "Gray"])
cinnamon = len(data[color == "Cinnamon"])
black = len(data[color == "Black"])
print(gray, cinnamon, black)

data_dict = {
    "Fur Color" : ["cinnamon", "gray", "black"],
    "Count" : [cinnamon, gray, black],
}
new_data = pd.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")


temp_list = []
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        if row[1] != "temp":
            temp_list.append(int(row[1]))
data = pd.read_csv("weather_data.csv")
datadict = data.to_dict()


temp_list = data["temp"].to_list()
average_temp = data["temp"].mean()
max_temp = data.temp.max()
 # data.temp.max can be used
day = data[data.temp == max_temp]
monday = data[data.day == "Monday"]
# print(monday.condition)
C = monday.temp
fahrenheit = (C * (9/5)) + 32

