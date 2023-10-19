"""
Chapter 1 : Exercise 7 : Even Numbers

Writing a program that prints the numbers from 1 to 100, but only prints the even numbers

"""

# start of the program

# initializing a variable num with 0, so the loop can 
num = 0

"""
# creating a while loop to print the numbers continously
while True:

    # a conditional statement to check if numbers printed are less than or equal to 100
    if num <= 100:
        # inrements a number by 1 if the above condition is true
        num += 1 
        
        # a nested conditon to check if the number is even
        if num % 2 == 0:
            print(num)

        continue # continue statement is used to let the compiler know that the loop should be continued

     # a condition that breaks the loop if the numbers to be printed are greater than 100   
    else:
        break # using break to break the loop

# end of the program 
"""

for num in range(0, 101):
    if num % 2 != 0:
        continue

    print(num)