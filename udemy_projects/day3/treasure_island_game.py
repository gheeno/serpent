treasure_island_start_message = input("What do you want to do to get to the treasure island? ")
lower_treasure_island_choice = treasure_island_start_message.lower()

if lower_treasure_island_choice == "study":
    print("Good! What do you want to study?")
    choice_study = input("what do you want to study? ")
    if choice_study.lower() == "python":
        print("Python! Great job! you'll get to the treasure island in no time!")
else:
    print("I recommend you study instead.")