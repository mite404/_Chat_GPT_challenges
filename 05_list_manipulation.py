# Challenge 5: List Manipulation
#
# Define a list of numbers. Write a program that prints the sum, average,
# maximum, and minimum of the numbers in the list.


# this was NOT the way to do it, LOL (╥﹏╥)
"""
nums = [3, 41, 12, 9, 74, 15]
print(len('The total items in this list are:', nums))

print(max('The highest number is:', nums))

print(min('The smallest number is:', nums))

print(sum('The sum of all numbers in this list is:', nums))

print(sum(nums)/len('The average of this list is:', nums))
"""

# this is the way to do it!
numbers = [3, 41, 12, 9, 74, 15]

# initialize variables
total_sum = 0
maximum = float('-inf')  # Set to negative infinity as an initial value
minimum = float('inf')  # Set to positive infinity as an initial value

# loop through the list
for number in numbers:
    # update the sum
    total_sum += number

    # update the maximum
    if number > maximum:
        maximum = number

    # update the minimum
    if number < minimum:
        minimum = number

# calculate the avg
average = total_sum / len(numbers)

# print the results
print('Sum:', total_sum)
print('Average:', average)
print('Maximum:', maximum)
print('Minimum:', minimum)
