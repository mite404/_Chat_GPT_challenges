# Challenge 10: FizzBuzz
# Write a program that prints the numbers from 1 to 20.
# For multiples of 3, print "Fizz" instead of the number,
# and for multiples of 5, print "Buzz."
#
# For numbers which are multiples of both three and five, print "FizzBuzz."


# Pseudocode workflow example:
'''
For each number from 1 to 20:
    If the number is divisible by both 3 and 5:
        Print "FizzBuzz"
    Else, if the number is divisible by 3:
        Print "Fizz"
    Else, if the number is divisible by 5:
        Print "Buzz"
    Else:
        Print the number
'''


# defining my own function
def fizzbuzz():
    for number in range(1, 21):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)


# ask user for input
while True:
    usernum = int(input('Please enter a number (0-20): '))
    if 1 <= usernum <= 20:
        break
    else:
        print('Ivalid input. Please enter a number between 0-20.')

    
# call the function
fizzbuzz()
