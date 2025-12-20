def greet(name):
    print(f"Hello, welcome to the program!, {name}")
    print("My Name is Herin")
    print("I am a python developer")

greet("Yash")

def greet_user(username , age):
    print(f"Hello {username}, you are {age} years old.")

greet_user("Yash" , 20) # positional argument

greet_user(age = "20" ,username = "Yash") # keyword argument