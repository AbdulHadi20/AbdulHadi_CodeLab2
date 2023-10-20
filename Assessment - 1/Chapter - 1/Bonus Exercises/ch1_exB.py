"""
Chapter 1 : Exercise B : Location List

Writing a program that does the following operations with the list given: 

- print the list and find the length of the list
- use sorted() to print the list in alphabetical order without changing the actual list
- show that the list is still in the original order
- use reverse() to reverse the order of the list
- print the list to show that the order has been changed
- use sort() to change the order to alphabetical order
- print the list to show that the order has been changed
- use sort () to reverse the order of the list
- print the list to show the order of the list has been changed

"""

# start of the program

locations =['Dubai','Paris', 'Switzerland', 'London', 'Amsterdam', 'New York']

# printing the list and finding the length of the list
print(f"\n The list of loactions : {locations} \n The length of the list is {len(locations)}.")

# using sorted to print the list in alphabetical order
print(f"\n The list in Alphabetical order: {sorted(locations)}")

# printing the list again to show its original order
print(f"\n The list in original order: {locations}")

# using reverse() to reverse the order and printing to show the order has been changed
locations.reverse()
print(f"\n The original list in reversed order is {locations}")

# using sort() to display the list in alphabetical order and printing it to show the order has been changed
locations.sort()
print(f"\n The original list in alphabetical order : {locations}")

# using sort() again to to reverse the order, then displaying the list
locations.sort(reverse = True)
print(f"\n The original list order has been reversed again : {locations}")

# end of the program

