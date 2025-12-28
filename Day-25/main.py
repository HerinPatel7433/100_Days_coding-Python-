import pandas 

data = pandas.read_csv("Day-25/weather_data.csv")
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

print(data["temp"].mean())

print(data["temp"].max())

# get data in row

print(data[data.temp == data.temp.max()])

monday = (data[data.day == "Monday"])
monday_temp = monday.temp[0]
monday_temp_fer = monday_temp * 9/5 + 32
print(monday_temp_fer)

# create a dataframe from scratch

data_dict = {
    "students": ["herin", "yash", "aditya"],
    "scores": ["99", "92", "97"]
}

data = pandas.DataFrame(data_dict)
data.to_csv("Day-25/new_data.csv", index=False)