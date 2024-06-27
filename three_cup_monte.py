from random import shuffle

cups = [" ", "O", " "]

def shuffle_list(cups):
    shuffle(cups)
    return cups

def user_choice():
    choice = ""
    while choice not in ["0", "1", "2"]:
        choice = input("Enter a choice from 0, 1, and 2: ")
    return int(choice)

def check_choice(cups, choice):
    if cups[choice] == "O":
        print(cups)
        print("Correct Guess!! You Win :)")
    else:
        print(cups)
        print("Incorrect Guess!!")

# Shuffle the cups
shuffled_cups = shuffle_list(cups)

# Get user's choice
user_choice_value = user_choice()

# Check the user's choice
check_choice(shuffled_cups, user_choice_value)