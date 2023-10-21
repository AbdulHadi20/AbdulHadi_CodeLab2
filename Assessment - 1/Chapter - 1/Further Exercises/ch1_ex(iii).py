"""
Chapter 1 : Exercise III : Arrows

Writing a program that prints the asterik pattern shown below

     *
    ***
   *****
  *******
 *********
    ***  
    ***
    ***

"""

# start of the program

rows = 5
# creating a loop to create the head of the arrow
for i in range(rows):
    for j in range(i, rows):
        print(" ", end = " ")

    for j in range(i + 1):
        print("*", end = " ")

    for j in range(i + 1):
        print("*", end = " ")

    print(" ")