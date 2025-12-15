print("Welcome to pizza deliveries")
size = input("what size pizza do you want? S, M or L: ")
bill = 0
pepperoni = input("Do you want pepperoni for an extra $2 on small pizza and $3 on medium or large pizza? Y or N ")
extra_chess = input("Do you want extra chess for an extra $1 on small pizza and $2 on medium or large pizza? Y or N ")

if size == "S" or size == "s":
    bill += 15
elif size == "M" or size == "m":
    bill += 20
elif size == "L" or size == "l":
    bill += 25
else: 
    print("invalid size")

if pepperoni == "Y" or pepperoni == "y":
    if size == "S" or size == "s":
        bill += 2
    else:
        bill += 3
if extra_chess == "Y" or extra_chess == "y":
    if size == "S" or size == "s":
        bill += 1
    else:
        bill += 2
print(f"your final bill is ${bill}")