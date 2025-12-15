# random module
import random
import my_module

random_integer = random.randint(0, 100)
print(random_integer)
print(my_module.my_favourite_number)

random_number_0_to_1 = random.random()
print(round(random_number_0_to_1,2))

random_float = random.uniform(1, 10)
print(round(random_float,2))
