"""
Chapter 1 : Exercise 2 : Maths

Writing a program that takes two numbers from the user, and calculates the following

1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus (%)

"""

#starting the program

# prompting the user to enter two numbers for the calculations
num1 = int(input("\n Please enter the first number = "))
num2 = int(input("\n Please enter the second number = "))

# now, performing calculations of the given numbers

add = num1 + num2  # addition
sub = num1 - num2  # subtraction
mul = num1 * num2  # multiplication
div = num1 / num2  # division
mod = num1 % num2  # modulus (remainder)

# now, displaying the output for each calculation

print("\n The addition of the two numbers is = ", add)
print("\n The subtraction of the two numbers is = ", sub)
print("\n The multiplication of the two numbers is = ", mul)
print("\n The division of the two numbers is = ", div)
print("\n The modulus (remainder) of the two numbers is = ", mod)

# end of the program