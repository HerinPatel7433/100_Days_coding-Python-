"""Error and Exceptions"""

try:
    file = open("Day-30//a_file.txt")
    a_dictionary = {"key": "Value"}
    print(a_dictionary["HERIN"])
except FileNotFoundError:
    file = open("Day-30//a_file.txt", "w")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was Closed.")