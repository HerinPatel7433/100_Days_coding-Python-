"""List Comprehension"""

number = [1, 2, 3]

number_list = [ n+1 for n in number]
print(number_list)

name = "herin"
letter_list = [letter for letter in name]
print(letter_list)

range_list = [num * 2 for num in range(1, 5)]
print(range_list)

names = ["Herin", "Yash", "Vansh", "Aditya", "Heneel", "Teesh"]

names_list = [name.upper() for name in names if len(name) == 5]
print(names_list)
