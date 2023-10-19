"""
Chapter 1 : Exercise 7 : Even Numbers

Writing a program that prints the numbers from 1 to 100, but only prints the even numbers

"""

# start of the program

# initializing a variable num with 0, so the loop can 
num = 0

# creating a for loop with range from 1 to 101
for num in range(1, 101):
    # using conditional statement to check if number is even or odd
    if num % 2 != 0: # if num is odd, then this condition will execute
        continue # since the num gets declared as odd, the continue statement helps skipping those numbers that are odd

    print(num) # prints the even numbers instead of odd

# end of the program