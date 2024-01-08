# Challenge 3: Even or Odd
#
# Write a program that checks if a given number is even or odd. The user
# should input the number.

try:
    num = int(input('Please enter a number:'))
    if (num % 2) == 0:
        print('The number is even')
    else:
        print('The number is odd')
except ValueError:
    print('Invalid input. Please enter a valid integer')
