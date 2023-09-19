# create a calculator to calculate the areas, circumfrences of circle, triangle, rectangle


# displaying and asking the user to en
optnshape = int(input(
    "Select a shape you want to calculate =  \n 1. Circle \n 2. Triangle \n 3. Rectangle"))

# calculates the circle
if optnshape == 1:
    optncal = int(
        input("What do you want to calculate? \n 1. Area \n 2. Circumfrence"))

    if optncal == 1:  # calculates the area of the circle
        radius = float(input("Enter the radius of the circle = "))
        pi = 3.14
        areacircle = pi * radius ** 2
        print("The area of the circle is ", areacircle, "sq. units.")

    elif optncal == 2:  # calculates the circumfrence of the circle
        radius = float(input("Enter the radius of the circle = "))
        pi = 3.14
        circumfrence = 2 * pi * radius
        print("The circumfrence of the circle is = ", circumfrence, "meters.")

# calculates the triangle
elif optnshape == 2:
    optncal = int(
        input("What do you want to calculate? \n 1. Area \n 2. Perimeter"))

    if optncal == 1:  # calculates the area of the triangle
        base = float(input("Enter the base of the triangle = "))
        height = float(input("Enter the height of the triangle = "))
        areatriangle = 1/2 (base * height)
        print("The area of the traingle is ", areatriangle, "sq. units.")

    elif optncal == 2:  # calculates the perimeter of the triangle
        side1 = float(input("Enter the first side of the triangle = "))
        side2 = float(input("Enter the second side of the triangle = "))
        side3 = float(input("Enter the third side of the triangle"))
        perimetertri = side1 + side2 + side3
        print("The perimeter of the traingle is = ", perimetertri, "meters.")

elif optnshape == 3:  # calculates the rectangle
    optncal = int(
        input("What do you want to calculate? \n 1. Area \n 2. Perimeter"))

    if optncal == 1:  # calculates the area of the rectangle
        length = int(input("Enter the length of the rectangle = "))
        width = int(input("Enter the width of the rectangle = "))
        arearect = length * width
        print("The area of the rectangle is = ", arearect, " sq. units")

    elif optncal == 2:  # calculates the perimeter of the the rectangle
        length = int(input("Enter the length of the rectangle = "))
        width = int(input("Enter the width of the rectangle = "))
        perimeterrect = 2 * (length + width)
        print("The perimeter of the rectangle is = ", perimeterrect, "meters.")

else:  # prints if user enters invalide values
    print("ERROR! PLEASE TRY AGAIN")
