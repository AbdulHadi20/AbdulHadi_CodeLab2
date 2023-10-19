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
random_list = [56, 88, 41, 77, 10, 9, 78, 68, 35, 50]

# using for loop to print the list
print("\n List Items: ")
for i in random_list:
    print("\n ", i)

# for printing the highest value, we use the max() function
print("\n The highest value in the list is: ", max(random_list))

# for printing the lowest value, we use the min() function
print("\n The lowest value in the list is: ", min(random_list))

# sorting the elements in ascending order
sorted_list = sorted(random_list)
print("\n Here is the list sorted in Ascending Order: ")
print("\n ",sorted_list)

# sorting the list in descending order
random_list.sort(reverse = True)
print("\n Here is the list sorted in Descending Order: ")
print("\n", random_list)

# appending two items in the list, then printing it
random_list.append(20)
random_list.append(99)

# now, printing the list after appending the two items
print("\n The list after two appended values: ")
print("\n ", random_list)

# end of the program 