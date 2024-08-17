price: int
age: int = int(input("enter age: "))

if age == 0:
    price = 10
elif age <= 18:
    price = 20
else :
    price = 30

print(f"You are {age} hence your ticket price is {price}")