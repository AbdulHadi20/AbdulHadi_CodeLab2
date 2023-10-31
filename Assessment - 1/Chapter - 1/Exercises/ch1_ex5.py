"""
Chapter 1 : Exercise 5 : Continue

Writing a program that impelements a while loop. The program keeps on running as long as the user presses 'y' when asked to continue.
Once the loop gets terminated, the output shows the number of times the loop got executed.

"""

# start of the program

# greeting the user
print("\n Welcome to the loop ! ")

# creating a function that asks the question
def question():
    global userentry
    userentry = str(input("\n Do you wish to continue ? (y/n) : "))
count = 1

# creating a while loop 
while True:
    question() # calling the function to ask the question
    if userentry == 'y': # executes if user enters y, loop keeps going
        count += 1        
        continue

    elif userentry == 'n': # executes if user enters n, loop terminates
        break

    else: # executes if user enters values other then y/n
        print("\n Invalid Entry. Please try again")

print(f"\n The loop has run {count} times now.")

# end of the program