"""
Chapter 1 : Exercise 7 : Even Numbers

Writing a program that prints the numbers from 1 to 100, but only prints the even numbers

"""

# start of the program

# initializing a variable num with 0, so the loop can 
num = 0

while True:
    if num <= 100:
        num += 1
        
        if num % 2 == 0:
            print(num)

            continue
        
    elif num > 100:
        break




"""    
while num <= 100:
    num += 1

    if num % 2 == 0:
        print(num)    

    continue
"""

# end of the program (NOT FINISHED)