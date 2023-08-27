print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#lower case letters
lower_name1 = name1.lower()
lower_name2 = name2.lower()

#dictionary
dict_true = {'t', 'r', 'u', 'e'}
dict_love = {'l', 'o', 'v', 'e'}

#steps 
#combine lower_name1 + lowername 2 to a dictionary
dict_lower_name1 = {letter: lower_name1.count(letter) for letter in lower_name1}
dict_lower_name2 = {letter: lower_name2.count(letter) for letter in lower_name2}

#combine dictionaries
combined_dictionaries = dict_lower_name1.copy()
for key, value in dict_lower_name2.items():
    combined_dictionaries[key] = combined_dictionaries.get(key, 0) + value

#compare the {t r u e} with {g h e e n o d a y l e}
common_letters_in_true = {key: value for key, value in combined_dictionaries.items() if key in dict_true}

#compare the {l o v e} with {g h e e n o d a y l e}
common_letters_in_love = {key: value for key, value in combined_dictionaries.items() if key in dict_love}

total_true = str(sum(common_letters_in_true.values()))
total_love = str(sum(common_letters_in_love.values()))

total_sum = total_true + total_love

if (int(total_sum)) < 10 or (int(total_sum)) > 90:
    print(f"Your score is {total_sum}, you go together like coke and mentos.")
elif (int(total_sum)) > 40 and (int(total_sum)) < 50:
    print(f"Your score is {total_sum}, you are alright together.")
else:
    print(f"Your score is{total_sum}.")