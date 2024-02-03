# The factorial function says to multiply all whole numbers from our
# number down to 1.
#
# Examples: 4! = 4 × 3 × 2 × 1 = 24.

def factorial(n):
    result = 1          # Initialize the result variable outside the loop

    while n > 1:        # Use a condition to control the loop
        result *= n     # Update the result variable by multiplying with the current value of n
        n -= 1          # Decrement n to move towards the base case

    return result       # Return the final result after the loop

# Test Cases
print(factorial(5))
print(factorial(0))
