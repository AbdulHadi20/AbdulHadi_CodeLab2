"""
Chapter 1 : Exercise 4 : Largest Number

Writing a program to prompt the user to enter three numbers, then printing the largest number of them all
using multiple if-else statements.

"""

# start of the program

# asking the user to enter the three numbers
num1 = int(input("\n Please enter the first number = "))
num2 = int(input("\n Please enter the second number = "))
num3 = int(input("\n Please enter the third number = "))

# using conditional statements to check the largest number
if num1 > num2 and num3: # will run if the first number is the largest
    print(f"\n The number {num1} is the largest number.")

elif num2 > num1 and num3: # will run if the second number is largest
    print(f"\n The number {num2} is the largest number.")

elif num3 > num1 and num2: # will run if the third number is the largest
    print(f"\n The number {num3} is the largest number.")

# end of the program
    