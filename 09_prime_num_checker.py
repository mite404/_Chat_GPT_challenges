# Challenge 9: Prime Number Checker
#
# Write a program that checks if a given number is a prime number or not. The
# user should input the number.


"""
Pseudocode to Find Prime Number
Start

   Input num

   Initialize variable temp = 0

   FOR loop = 2 to num/2

      IF num is divisible by loop

         Increment temp

      END IF

   END FOR

      IF temp is equal to 0

         RETURN “Num IS PRIME”

      END IF

      ELSE

         RETURN “Num IS NOT PRIME”

      END ELSE

End
"""


num = int(input('Enter a number: '))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, ' is not a prime number')
            print(i, "times", num//i, "is", num)
            break
        else:
            print(num, "is a prime number")
else:
    print(num, " is not a prime number")
