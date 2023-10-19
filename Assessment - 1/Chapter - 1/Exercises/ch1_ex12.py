"""
Chapter 1 : Exercise 12 : Area Function

Writing a program that displays a menu and asks the user to select from the following options:

1. Calculate the area of the square
2. Calculate the area of the circle
3. Calculate the area of the triangle

"""

# start of the program

# creating a function to calculate the area of a square
def areasq():
    # displaying the user's selection
    print("\n You have selected to find the area of a square.")

    # asking for the required values
    sidesq = float(input("\n Please Enter the side of the square = "))

    # formula to find the area of the square
    sqarea = sidesq * sidesq

    # printing the results
    print(f"\n The area of the square with sides {sidesq} is {sqarea} m. sq.")


# creating a function to calculate the area of a circle
def areacirc():
    # displaying the user's selection
    print("\n You have selected to find the area of a circle.")

    # asking the users for required values
    radius = float(input("\n Please Enter the radius of the circle = "))
    
    #declaring the value of pi, and using the circle formula
    pi = 3.14
    circarea = pi * radius**2

    # printing the results
    print(f"\n The area of the circle with radius of {radius} is {circarea} m. sq.")


# creating a function to calculate the area of a triangle
def areatri():
    # displaying the user's selection
    print("\n You have selected to find the area of a triangle.")

    # asking for required values
    base = float(input("\n Please Enter the base of the triangle = "))
    height = float(input("\n Please Enter the height of the triangle = "))

    # using the formula to find the area of the triangle
    triarea = 0.5 * base * height

    # printing the results
    print(f"\n The area of the triangle with base {base} and height {height} is {triarea} m. sq.")


# creating a function that works based on the options selected by the user
def optn():
    # asking for the users input
    useroptn = int(input("\n 1. Find the area of a square \n 2. Find the area of a circle \n 3. Find the area of a triangle \n "))
    
    # condtiotional statements, based on the user's selection
    if useroptn == 1: # runs if user presses 1
        areasq()
        
    elif useroptn == 2: # runs if user presses 2
        areacirc()
        
    elif useroptn == 3: # runs if user presses 3
        areatri()
        
    else: # runs if user fails to follow instructions provided
        print("\n Invalid entry, please try again")
        optn()


# a welcome message
print("\t Welcome to the shape area calculator ! \n Please select from the options for the calculation of the desired shape.")
# calling the optn() funtion 
optn()

# end of the program