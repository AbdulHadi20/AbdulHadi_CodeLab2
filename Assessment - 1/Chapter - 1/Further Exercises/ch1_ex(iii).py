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

# making the triangle part (the top part) of the arrow

# creating a var to set the number of max. asteriks in a row
aster = 9

# creating a for loop that runs until the max. num of asteriks are allowed in a line is reached
for i in range(1, aster + 1, 2):
    # printing the asteriks, the spaces first
    # the spaces automatically get reduced by 1, means the next line will have more asteriks
    print(" "*(aster - 1), "*"*i)
    # after printing an asterik in a line, the asterik gets reduced by 1
    aster = aster - 1

# now, creating a for loop to print the line part of the arrow
for i in range(1,5):
    # prints the asteriks after 7 spaces
    print(" "*7, "***")

# end of the program