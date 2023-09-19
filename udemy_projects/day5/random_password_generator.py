#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


def get_item_list_randomized(list_, amount_of_items):
    result = []
    for num in range(amount_of_items):
        random_index = random.randint(0, len(list_) - 1)
        result.append(list_[random_index])
    return result


if __name__ == "__main__":
    letters_ = get_item_list_randomized(letters, nr_letters)
    numbers_ = get_item_list_randomized(numbers, nr_symbols)
    symbols_ = get_item_list_randomized(symbols, nr_numbers)
    combined_list = letters_ + numbers_ + symbols_
    randomized_list = random.sample(combined_list, len(combined_list))
    password = ''.join(map(str, randomized_list))
    print(password)
