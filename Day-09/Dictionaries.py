# Dictioaries and Nesting
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, 
# and they have keys and values.

# Creating a dictionary

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from a dictionary

print(programming_dictionary["Bug"])

# Adding new items to a dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

# looping through a dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])