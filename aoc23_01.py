# Advent of Code 2023
# Day 1, problem 1

# I spent about fifteen minutes considering doing this up with regex with the re.search(), because as a young man I
# did a lot of perl for some terrible reason and it used to feel like second nature.  You know what I don't need
# to spend voluntary time with these days? perl regex constructions.  Let's do this like a sane human being instead.

import string


def problem_one():
    file = open("input_01.txt")
    total = 0
    for line in file:
        first_digit = None
        last_digit = None
        # let's do this a really straightforward way: just march through the string looking for digit characters
        # and doing a little accounting when we find one.
        for char in line:
            if char in string.digits:
                if not first_digit:
                    first_digit = int(char)
                else:
                    last_digit = int(char)

        calib_val = 10 * first_digit
        if last_digit:
            calib_val += last_digit
        else:
            calib_val += first_digit

        total += calib_val

    print(f'Problem one -- Total: {total}')


def problem_two():
    file = open("input_01.txt")
    total = 0
    the_set = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
               '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    for line in file:
        first_digit = 0
        first_index = 99999
        last_digit = 0
        last_index = -1
        # okay, a little fancier this time since per-character searches won't work anymore: set up a dictionary of both
        # digits and number words, and then use find and rfind to search for each dictionary key to find out if it
        # breaks the current record for early or late number in the string.
        for key in the_set:
            index = line.find(key)
            if index > -1 and index < first_index:
                first_index = index
                first_digit = the_set[key]

            index = line.rfind(key)
            if index > -1 and index > last_index:
                last_index = index
                last_digit = the_set[key]

        calib_val = (10 * first_digit) + last_digit
        total += calib_val

    print(f'Problem two -- Total: {total}')


problem_one()
problem_two()
