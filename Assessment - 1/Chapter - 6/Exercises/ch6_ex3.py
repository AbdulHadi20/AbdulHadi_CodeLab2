"""
Chapter 6 : Exercise 3 : Calculator

Write a program that will display the following calculator menu

1. Add
2. Subtract
3. Multiply
4. Divide
5. Modulus
6. Check greater number

The program will prompt the user to choose the operation choice (from 1 to 6). Then it asks the user to input values for the calculation. 
The program outputs the results of the calculation.Use operator module functions

"""

# start of the program

import math

# creating a function for the calulator menu

def calculate():
    print(f"\n Select what operation do you want to perform: \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Modulus \n 6. Check Greater Number")


# creating a while loop, to keep the program running until the user quits
while True:
    # calling the function
    calculate()
    
    # asks the user to enter the choice or quit
    user_choice = (input("\n Select your choice of operation or press q to quit = "))

    # condition based on user's selection
    if user_choice == 'Q' or user_choice == 'q': # runs if user quits
        print("\n You Quit")

        break # loop terminated

    user_choice = int(user_choice)     # converts to integer

    if 1 <= user_choice <= 6: # runs if user selects a valid option
        val1 = int(input('\n Enter the first value = '))
        val2 = int(input('\n Enter the second value = '))

        if user_choice == 1: # runs if user wants the sum
            print(f"\n The sum of {val1} and {val2} is {val1 + val2}")

        elif user_choice == 2: # runs if user wants the difference
            print(f"\n The difference of {val1} and {val2} is {val1 - val2}")

        elif user_choice == 3: # runs if user wants the product
            print(f"\n The product of {val1} and {val2} is {val1 * val2}")

        elif user_choice == 4: # runs if user wants the division    
            print(f"\n The division of {val1} and {val2} is {val1 / val2}")

        elif user_choice == 5: # runs if user wants the remainder/modulus                                          
            print(f"\n The modulus of {val1} and {val2} is {val1 % val2}")

        elif user_choice == 6: # runs if user wants to know which number is greatest
            if val1 > val2: # nested conditional, checks and prints the largest number
                print(f"\n {val1} is greater than {val2}")

            elif val1 == val2: # runs if both values are equal
                print(f"{val1} is equal to {val2}")

            else: # runs if the first and second conditions are not true
                print(f"\n {val2} is greater than {val1}")

    else: # runs if user tries to enter a random value
        print("\n Invalid Input. Try again")
        
# end of program
