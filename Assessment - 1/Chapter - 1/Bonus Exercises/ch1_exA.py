"""
Chapter 1 : Exercise A : Multiplication Tables

Writing a program that prints the tables from 1 to 10. The format is as follows:

Multiplication table of : 1

1 x 1 = 1
...
1 x 10 = 10

...

Multiplication table of : 10

1 x 10 = 10
...
10 x 10 = 100

"""

# start of the program

# initializing the table, this var will be used to display the table
table = 1


# creating a while loop to print the tables from 1 to 10
while table <= 10:
    # diplaying the table number on top of each table
    print(f"\n Multiplication table of: {table}")

    # creating a nested for loop inside while to print each table from 1 to 20
    for i in range(0, 10):
        # increments i by 1
        i = i + 1
        
        # calculations of tables
        ans = i * table

        # printing the result
        print(f" {i} x {table} = {ans}")

    # table being incremented by 1, after a table has been complete    
    table += 1

# end of the program