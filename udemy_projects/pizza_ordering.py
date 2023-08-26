print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

#size_pricer
size_price = 0
if size == "S":
    size_price = 15
elif size == "M":
    size_price = 20
elif size == "L":
    size_price = 25
else:
    size_price

#pepperoni_pricer
pepperoni_price = 0
if add_pepperoni == "Y":
    if size == "S":
        pepperoni_price = 2
    else:
        pepperoni_price = 3
else:
    pepperoni_price

#extra_cheese_pricer
extra_cheese_price = 0
if extra_cheese == "Y":
    extra_cheese_price = 1
else:
    extra_cheese_price

bill = size_price + pepperoni_price + extra_cheese_price
print(f"Your final bill is: ${bill}.")