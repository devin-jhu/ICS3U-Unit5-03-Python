#!/usr/bin/env python3

# Created by Devin Jhu
# Created on May 2022
# The counter


def percentage(level):
    # this function converts a level to percentage

    # process
    if level == "4+":
        percentage_number = 97

    elif level == "4":
        percentage_number = 91

    elif level == "4-":
        percentage_number = 83

    elif level == "3+":
        percentage_number = 78

    elif level == "3":
        percentage_number = 75

    elif level == "3-":
        percentage_number = 71

    elif level == "2+":
        percentage_number = 68

    elif level == "2":
        percentage_number = 65

    elif level == "2-":
        percentage_number = 61

    elif level == "1+":
        percentage_number = 58

    elif level == "1":
        percentage_number = 55

    elif level == "1-":
        percentage_number = 51

    elif level == "R":
        percentage_number = 30

    else:
        percentage_number = 0

    return percentage_number


def main():
    # this function gets input, calls a function, gives output

    # input
    level = input("Enter level: ")

    percentage_number = percentage(level)

    if percentage_number == 0:
        print("not a percentage")
    else:
        print("Level {0} is {1}%.".format(level, percentage_number))

    print("\nDone.")


if __name__ == "__main__":
    main()
