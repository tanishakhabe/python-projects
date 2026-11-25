import random, sys

# Load a list of first names
first_names = ("noodle", "waffle", "bubble", "muffin", "doodle", "biscuit")

# Load a list of last names
last_names = ("snickerdoodle", "flapjack", "pumpernickel", "sprinkles")

while True: 
    # Choose a first name at random


    # Assign the name to a variable
    first_name = random.choice(first_names)

    # Choose a last name at random


    # Assign the name to a variable
    last_name = random.choice(last_names)


    # Print the names to the screen in order and in red font
    print(f"\033[31m{first_name} {last_name}\033[0m", file=sys.stderr)

    # Ask the user to quit or play again
    user_input = input("Do you want to quit or play again?")

    # If user plays again: 
        # repeat
    if user_input.lower() == "quit": 
        break

    # If user quits:
        # end and exit 