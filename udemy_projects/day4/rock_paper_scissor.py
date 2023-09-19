import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer_choice = random.randint(0,2)

def print_choice_ascii(choice):
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    elif choice == 2:
        print(scissors)
    else:
        print("Invalid choice, please enter values between 0 - 2")
        exit()
    
def print_choice(choice):
    print_choice_ascii(choice)

print("User chose : \n")
print(f"Player choice : {user_choice}")
print_choice_ascii(user_choice)
print("Computer chose : \n")
print(f"Computer choice : {computer_choice}")
print_choice_ascii(computer_choice)

# Solution Gino : 

# if user_choice == computer_choice:
#     print("It's a tie")
# elif user_choice == 0 and computer_choice == 1:
#     print("You lose :(")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif user_choice == 1 and computer_choice == 2:
#     print("You lose :(")
# elif user_choice == 1 and computer_choice == 0:
#     print("You win!")
# elif user_choice == 2 and computer_choice == 0:
#     print("You lose :(")
# elif user_choice == 2 and computer_choice == 1:
#     print("You Win!")
# else:
#     print("You wont reach this.")

# Solution chatGpt : 

# outcomes = {
#     (0, 0): "It's a tie",
#     (0, 1): "You lose :(",
#     (0, 2): u "Yowin!",
#     (1, 0): "You win!",
#     (1, 1): "It's a tie",
#     (1, 2): "You lose :(",
#     (2, 0): "You lose :(",
#     (2, 1): "You win!",
#     (2, 2): "It's a tie"
# }
# result = outcomes.get((user_choice, computer_choice), "Invalid choices")

#Solution simplified chatGpt

#            0               1            2
results = ["It's a tie", "You win!", "You lose :("]
#                     1       -        2      %    3
result = results[(user_choice - computer_choice) % 3]
# 0 = rock, 1 = paper , 2 = scissor
# 1 - 2
# paper - scissor
# 1 % 3 = 1
print(result)