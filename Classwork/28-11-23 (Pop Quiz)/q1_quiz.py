"""
Writing a program to print the following pattern

1
12
123
1234

"""

# start of the program

# initializing the number of rows needed
rows = 4

# creating an outer for loop for the rows
for i in range(1, rows + 1):

    # creating an inner loop, that prints the coloumns 
    for j in range(1, i + 1):
        # prints the numbers in the columns
        print(j, end = ' ') # the end is used to add space

    print(' ') # is printing the numbers in a new line

# end of the program