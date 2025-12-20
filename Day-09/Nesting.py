# Nesting

# Nesting is the concept of having a collection inside another collection. In Python, you can nest lists, dictionaries,
#  and sets inside other lists, dictionaries, and sets.


capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
}

travel_log = {
    "France": {"num_times_visitd": 8,"cities_visited": ["Paris", "Lille", "Dijon"],},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    "Italy": ["Rome", "Milan", "Venice"],
}

print(travel_log["Germany"][1]) # Output: Lille
print(travel_log["France"]["cities_visited"][2]) # Output: Dijon

nested_list = ["A" , "B", ["C1", "C2", "C3"], "D"]

print(nested_list[2][1]) # Output: C2