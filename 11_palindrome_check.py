# Challenge 1: Palindrome Checker
#
# Write a Python function that checks if a given string is a palindrome.
# A palindrome is a word, phrase, number, or other sequence of characters
# that reads the same forward and backward, ignoring spaces, punctuation,
# and capitalization.
import re


def askforString():             # ask user to enter a string
    s = input('Please enter a palindrome: ')
    return s


def is_palindrome(s):
    # convert the string to lowercase
    s = s.lower()

    # remove non-alphanumberic chars
    s = re.sub(r'\W+', '', s)

    # check if the string is a palindrome
    reversed_s = s[::-1]

    if s == reversed_s:
        print(f"{s} is a palindrome!")
    else:
        print(f"{s} is not a palindrome, please try again.")


def main():                     # calling the functions
    user_input = askforString()
    is_palindrome(user_input)


# calling the main function
if __name__ == "__main__":
    main()
