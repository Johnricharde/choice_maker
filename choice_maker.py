import random


def main():
    print(compare_all(get_options()))


def get_options():
    options = []
    print("Insert your options. \nType 'done' when you are finished:")

    # Gets all options from the user
    while True:
        option = input("Insert an option: \n")
        if option.lower() == "done":
            break
        options.append(option)
    return options


# Takes a list of options and returns one option
def compare_all(options):
    if len(options) == 1:
        return options[0]
    
    options.remove(compare_pair(options[0], options[1]))


def compare_pair(option_1, option_2):
    if random.random() < 0.5:
        return option_1
    else:
        return option_2


# print(get_options())
main()