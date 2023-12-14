"""
Chapter 4 : Exercise 3 : Reading to a list

The file numbers.txt has a list of 100 integer numbers each on a newline. 
Create a python program that puts this data into a list, then output the values in integer format.

"""

# opening and reading the file that contains the numbers 1 - 100
with open('numbers.txt', 'r') as file:
    # using for loop to read each line, and convert each line into integer, and storing it in the list
    num_list = [int(line.strip()) for line in file] 

# displaying the outphut (the list of numbers, convertied from strings to integers)
print("\n Displaying the list of numbers in integer format = ")
print(num_list)

# end of the program