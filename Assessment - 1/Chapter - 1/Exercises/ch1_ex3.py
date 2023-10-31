"""
Chapter 1 : Exercise 3 : Is it Triangle ?

Writing a program that asks the user to enter the three sides of a triangle. Then the triangle inequality is used to determine 
wether the length of the sides actually make a triangle. (Tip: The length of two sides must be equal to or greater than of the 
remaining side).

Extension:
Since the triangle has been validated, now we determine the type of the triangle. Equilateral, Isosceles, Scalene.

"""

# start of the program

# asking the user to enter the length of the three sides
side1 = float(input("\n Please enter the length of the first side of the triangle = "))
side2 = float(input("\n Please enter the length of the second side of the triangle = "))
side3 = float(input("\n Please enter the length of the third side of the triangle = "))

# since the length of any two sides must be greater than or equal to the remaining side, we use the triangle inequality function formula 
sum1 = side1 + side2
sum2 = side2 + side3
sum3 = side1 + side3

# using conditional statements to check if the sides make a triangle
# if the triangle has the sum of any two sides greater or equal to than the remaining side, this statement will executed
if side1 <= sum2 and side2 <= sum3 and side3 <= sum1: 
    print(f"\n The length of the three sides {side1, side2, side3} make a triangle.")

    # checking the type of the triangle
    if side1 == side2 == side3: # will execute if all sides are equal
        print("\n This triangle is an equilateral triangle, because it has all three sides equal.")

    elif side1 == side2 or side2 == side3 or side3 == side1: # will execute if two sides are equal
        print("\n This triangle is an isosceles triangle, because it has two sides equal.")

    else: # will execute if none of the sides are equal
        print("\n This triangle is a scalene triangle, because it has no sides equal.")

# this statement will execute if the statement above is false
else:
    print(f"\n The three sides {side1, side2, side3} do not make a triangle")

# end of the program