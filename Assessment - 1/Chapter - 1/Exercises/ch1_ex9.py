"""
Chapter 1 : Exercise 9 : Integer List

Writing a program that creates a list, then does the following things: 

- Create a list with 10 items
- Output the list using for loop
- Output the highest and lowest value
- Sort the elements in ascending order
- Sort the elements in descending order
- Append two items
- print the list after appending

"""

# start of the program

# creating the list with 10 items
random_list = ['Pakistan', 'Portugal', 'Argentina', 'UAE', 'USA', 'India', 'New Zealand', 'Canada', 'Spain', 'Germany']

# using for loop to print the list
print("\n List Items: ")
for i in random_list:
    print("\n ", i)

# printing the highest and lowest values


# sorting the elements in ascending order
sorted_list = sorted(random_list)
print("\n Here is the list sorted in Ascending Order: ")
print("\n ",sorted_list)

# sorting the list in descending order (not working yet)
reversed_list = reversed(random_list)
print("\n Here is the list sorted in Descending Order: ")
print("\n", reversed_list)

# appending two items in the list, then printing it
newlist = random_list.append('France', 'Belgium')
print(newlist)
