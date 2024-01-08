# Challenge 4: Celsius to Fahrenheit
#
# Create a program that converts a temperature in Celsius to Fahrenheit. The
# user should input the temperature in Celsius.

try:
    cel = int(input('Please enter a temperature in Celsius to convert to Fahrenheit:'))
except ValueError:
    print('Invalid input. Please enter a valid integer')

far = cel * (9/5) + 32
print('Here is the temperature converted to F:', far)
