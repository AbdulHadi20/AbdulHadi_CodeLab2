"""
Chapter 1 : Exercise 13 : Product of list items

Writing a program that passes a list as an argument in a function. The function then multiplies the values and displays
the output.

"""

# start of the program

# creating a list of 5 numbers
nums = [3, 8, 4, 5, 2]

# creating a function, with a variable ans initialized as 1 in the paranthesis
def multiply(prod = 1):
    # creating a for loop to go through the list
    for i in nums:
        # multiplying the elements in the list
        prod = prod * i

    # printing the result
    print(f"\n The product of all values in the list is {prod}")

# calling the function
multiply()

# end of the program