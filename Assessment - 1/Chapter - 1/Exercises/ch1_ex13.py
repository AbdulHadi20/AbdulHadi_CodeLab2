"""
Chapter 1 : Exercise 13 : Product of list items

Writing a program that passes a list as an argument in a function. The function then multiplies the values and displays
the output.

"""

# start of the program

# importing the math library
import math

# creating a list of 5 numbers
nums = [3, 8, 4, 5, 2]

# using the math.prod() function to multiply all the numbers in the list
prod = math.prod(nums)

# printing the list
print(f"\n The list: {nums}")

# printing the result
print(f"\n The product of all the values in the list is {prod}")

# end of the program