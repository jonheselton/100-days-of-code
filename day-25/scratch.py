##!/usr/bin/python
import csv
import pandas

# temperatures = []
# with open('weather_data.csv') as f:
#     weather_data = csv.reader(f)
#     for row in weather_data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))

# print(temperatures)

# data = pandas.read_csv('weather_data.csv')
# # temperature_list = data['temp'].to_list()
# # average = sum(temperature_list) / len(temperature_list)
# # print(average)
# #average = data['temp'].mean()
# #print(data['temp'].max())

# #print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# f = int(monday.temp.multiply(9).divide(5).add(32))
# print(f)

squirrels = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey = squirrels[squirrels['Primary Fur Color'] == 'Gray']
red = squirrels[squirrels['Primary Fur Color'] == 'Cinnamon']
black = squirrels[squirrels['Primary Fur Color'] == 'Black']

output = { "Fur Color" : ['gray', 'red', 'black'], 'count': [len(grey.index), len(red.index), len(black.index)]}
pandas.DataFrame(output).to_csv('squirrel_data.csv')


def main():
    pass

if __name__ == "__main__":
    main()
    
    