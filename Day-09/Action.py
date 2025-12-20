import Action_art

Action_data = {}

print(Action_art.logo)
print("Welcome to the Secret Auction Program.")

bidding_finished = False

def find_highest_bidder():
    if should_continue == "no":
        bidding_finished = True
        highest_bidder = ""
        highest_bid = 0
        for bidder in Action_data:
            bid_amount = Action_data[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                highest_bidder = bidder
        print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
    elif should_continue == "yes":
        print("\n" * 50)
        print("*************************Next Bidder*************************")  
    else:
        print("Invalid input. Please type 'yes' or 'no'.")  

while not bidding_finished:
    input_name = input("What is your name?: ")
    input_bid = int(input("What is your bid?: $"))
    Action_data[input_name] = input_bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    find_highest_bidder(Action_data)