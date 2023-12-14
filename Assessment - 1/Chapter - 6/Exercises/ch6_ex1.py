"""
Chapter 6 : Exercise 1 : Basic Math

Using math module compute the following

- For a =2.3 find the ceil of a
- For a =2.3 find the floor of a
- For a = 5 find the factorial of a
- Find the value of 23
- For a=16 find the square root of a

"""

#  start of the program

# importing the required module
import math

# initializing the given values in a variable
num1 = 2.3
num2 = 5
num3 = 16

# using the module, to get the results of the num1:
# ceil 
ansOfCeil = math.ceil(num1)

# floor 
ansOfFloor = math.floor(num1)

# printing the floor and ceiling
print(f"\n The ceil of {num1} is {ansOfCeil} \n The floor of {num1} is {ansOfFloor}")


# now, getting the factorial of the num2:
fact_num2 = math.factorial(num2)

# getting the result
print(f"\n The factorial of {num2} is {fact_num2}")


# getting the square root of the third number
sqrt_num3 = math.sqrt(num3)

# getting the result
print(f"\n The square root of {num3} is {sqrt_num3}")

# end of the program