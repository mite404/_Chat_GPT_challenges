# Challenge 2: Sum of Two Numbers
#
# Create a program that takes two numbers as input from the user and prints
# their sum.

try:
    num1 = int(input('Please enter a number:'))
    num2 = int(input('Please enter another number:'))
except ValueError:
    print('Invalid input. Please enter a valid integer')

sum = num1 + num2
print(sum)
