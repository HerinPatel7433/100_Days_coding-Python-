def format_name(first_name, last_name):
    return f"{first_name.title()} {last_name.title()}"

first = input("What is your first name? ")
last = input("What is your last name? ")

print(format_name(first, last))

