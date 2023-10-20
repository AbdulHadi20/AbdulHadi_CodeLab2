"""
Chapter 1 : Exercise C : Calculator Function

Writing a program that prompts to select options from the menu for the calculations. The user is asked in the end
if they wish to continue with the calculations

"""

# start of the program

# importing the math library
import math

################################ creating the addition function #####################################
def addfunction():
    # letting the user know of their selection
    print("\n You decided to perform addition")

    # creating an empty list to save the user's values
    addlist = []

    # asking the user to enter values
    def addvalues():
        values = float(input("\n Please Enter the value you wish to calculate = "))
        addlist.append(values) # appends the entered value in the list
    
    # calling the function
    addvalues()

    # creating a while loop to ask the user if they wish to add more values
    while True:
        # asking the user if they need more values
        more = str(input("\n Do you wish to add more values (y/n) = ")) # asking if user wants to add more values

        # conditions based on user's answer
        if more == 'y': # runs if user presses y
            addvalues()

        elif more == 'n': # runs if user presses n
            break

        else: # runs if user presses any button
            print("\n Invalid Entry, please try again")
            addvalues()

    # using the sum() to add the elements in the list
    print(f"\n The sum of the numbers {addlist} is {sum(addlist)}")

################################# creating the multiplication function ########################################
def mulfunction():
    # letting the user know of their selection
    print("\n You decided to do multiplication")

    # creating an empty list to store user's values
    mullist = []

    # asking the user to add values
    def mulvalues():
        values = float(input("\n Please Enter the value you wish to calculate = "))
        mullist.append(values) # appends the entered value in the list

    # calling the function
    mulvalues()

     # creating a while loop to ask the user if they wish to add more values
    while True:
        # asking the user if they need more values
        more = str(input("\n Do you wish to add more values (y/n) = ")) # asking if user wants to add more values

        # conditions based on user's answer
        if more == 'y': # runs if user presses y
            mulvalues()

        elif more == 'n': # runs if user presses n
            break

        else: # runs if user presses any button
            print("\n Invalid Entry, please try again")
            mulvalues()

    # printing the result using math.prod() function, from the math library
    print(f"\n The product of the numbers {mullist} is {math.prod(mullist)}")

######################################## creating the subtraction function #############################

def subfunction():
    # letting the user know of their selection
    print("\n You decided to do subtraction")

    # asking the user for the values
    num1 = float(input("\n Please enter the first value = "))
    num2 = float (input("\n Please enter the second value = "))

    # calculations
    sub = num1 - num2

    # printing the result
    print(f"\n The difference of {num1} and {num2} is {sub}")

####################################### creating the division function ################################

def divfunction ():
    # letting the user know of their selection
    print("\n You decided to do division")

    # asking the user for the values
    num1 = float(input("\n Please enter the first value = "))
    num2 = float (input("\n Please enter the second value = "))

    # calculations
    div = num1 / num2

    # printing results
    print(f"\n The answer is : {div}")

################################## creating the modulus function #######################################

def modfunction():
    # letting the user know of their selection
    print("\n You decided to find the modulus")

    # asking the user for the values
    num1 = float(input("\n Please enter the first value = "))
    num2 = float (input("\n Please enter the second value = "))

    # calculations
    mod = num1 % num2

    # printing results
    print(f"\n The answer is : {mod}")

#######################################################################################################

# user greeting
print("\t WELCOME TO THE CALCULATOR ! \n Please select any of the options below ")

# creating a loop to keep asking the user once an option has been executed
while True:
    # asking the user to select an option
    usersel = int(input("\n 1. Addition \n 2. Multiplication \n 3. Subtraction \n 4. Division \n 5. Modulus \n "))\
    
    # conditional statements
    if usersel == 1: # runs if user presses 1
        addfunction()

    elif usersel == 2:  # runs if user presses 2
        mulfunction()

    elif usersel == 3:  # runs if user presses 3
        subfunction()

    elif usersel == 4:  # runs if user presses 4
        divfunction()

    elif usersel == 5:  # runs if user presses 5
        modfunction()

    else:  # runs if user presses any other button
        print("\n ERROR")

    # asking the user if they wish to continue

    continu = str(input("\n Do you wish to continue the calculations (y/n) = "))

    # conditional statements
    if continu == 'y':
        continue

    elif continu == 'n':
        break

    else:
        print("\n ERROR")

        continue

# end of the program