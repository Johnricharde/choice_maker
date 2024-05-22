import random


def main():
    print(compare_all(get_options()))


def get_options():
    print("Insert your options. \nType 'done' when you are finished:")
    options = []

    # Gets all options from the user
    while True:
        option = input("Insert an option: \n")
        if option.lower() == "done":
            break
        options.append(option)

    return options


# Takes a list of options and returns one option
def compare_all(options):
    while len(options) > 1:
        winner = compare_pair(options.pop(0), options.pop(0))
        options.append(winner)

    return options[0]


# Returns one of the two arguments
def compare_pair(option_1, option_2):
    return option_1 if random.random() < 0.5 else option_2


main()