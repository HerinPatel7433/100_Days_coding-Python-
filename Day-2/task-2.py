#Type error example

# print(len(123)) # This will raise a TypeError because len() expects a string, list, or other iterable, not an integer.
print(len("123"))  # This will work correctly and print 3

#Checking data types

print(type("Hello"))  # This will print <class 'str'>
print(type(123))      # This will print <class 'int'>
print(type(123.0))    # This will print <class 'float'>
print(type(True))     # This will print <class 'bool'>

#Type conversion

print(int("123") + int("456"))
print(float("123.0") + float("456.0"))  

print("Number of latter in your name:" + str(len(input("What is your name? "))))
