"""
Chapter 1 : Exercise II : Sum of Digits in a Number

Writing a  program that prints the sum of digits in a number.
Ex : If user enter 46594, so result should be 4 + 6 + 5 + 9 + 4 = 28

"""

# start of the program

# asking the user to enter random numbers
num = input("\n Please enter any random numbers = ")

# setting an empty variable to save the result
sum = 0

# creating a loop to convert the string variables into integer datatype
for i in num:
    intnum = int(i)
    
    # adding each number 
    sum = sum + intnum

# printing the result
print(f"\n The sum of {num} is {sum}")

# end of the program 