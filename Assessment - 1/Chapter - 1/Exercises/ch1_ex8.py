"""
Chapter 1 : Exercise 8 : Print Pattern

Writing a program that prints the following pattern 

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""

# start of the program

# setting the number of rows to be added
rows = 5

# using for loop to create the rows
for i in range(1, rows + 1):
    # using a nested for loop to create columns
    for j in range(1, i + 1):
        print(j, end = ' ') # prints the columns, end function to add space

    print(" ") # using print with " " to print numbers in a new line


# end of the program