"""
Write a program to print  the factorial of the given number

"""


# start of the program 

# asking the number from the user 
user_num = int(input("\n Please Enter any number = "))

# initializing the factorial to one
fact = 1

# creating a for loop, to add the numbers upto the entered number by the user
for i in range(1, user_num + 1):
    fact = fact * i # multiplies the factorials


# prints the result 
print(f'\n The factorial of the number {user_num} is {fact}')

# end of the program