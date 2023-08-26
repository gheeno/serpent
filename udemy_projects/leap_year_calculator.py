"""To determine whether a year is a leap year, follow these steps:

1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
4. The year is a leap year (it has 366 days).
5. The year is not a leap year (it has 365 days).
"""
year = int(input("Which year do you want to check? "))
#evenly divisible means no remainder.

modulus_divide_by_4 = year % 4
modulus_divide_by_100 = year % 100
modulus_divide_by_400 = year % 400

if modulus_divide_by_4 == 0:
    #step 2
    if modulus_divide_by_100 == 0:
        #step 3
        if modulus_divide_by_400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year")
else:
    print("Not leap year.")