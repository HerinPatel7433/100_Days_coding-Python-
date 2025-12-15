def calculate_love_score(name_1, name_2):
    combined_names = (name_1 + name_2).lower()
    
    true_count = sum(combined_names.count(letter) for letter in "true")
    love_count = sum(combined_names.count(letter) for letter in "love")
    
    love_score = int(f"{true_count}{love_count}")
    
    print(f"Your love score is: {love_score}")

calculate_love_score("Kanye West", "Kim Kardashian")