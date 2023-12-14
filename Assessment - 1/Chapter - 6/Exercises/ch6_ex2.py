"""
Chapter 6 : Exercise 2 : Numpy Array

For the array a = [20,23,82,40,32,15,67,52] print the output of following

- find the indices of even numbers
- Sort the array
- Slice elements from index 3 to the end of the array
- Slice elements from index 0 to index 4
- print [32 15 67] using negative slicing

"""

# start of the program

# importing the required library/module
import numpy as np  

# the given list
given_list = [20, 23, 82, 40, 32, 15, 67, 52]
print(f"\n The given list is {given_list}")

# converting the given list into an array
given_list = np.array(given_list)

# finding the indices of the numbers 
indices = np.where(given_list % 2 == 0)
print(f"\n Indices of even numbers is {indices[0]}")

# sorting the array
sort_array = np.sort(given_list)
print(f"\n The sorted list is {sort_array}")

# slicing the array from index 3
slice_array1 = given_list[3:]
print(f"\n The first slicing is {slice_array1}")

# slicing the list from element 0 - 4
slice_array2 = given_list[:5]
print(f"\n The second slicing is {slice_array2}")

# slicing the array from [32 15 67] using -ve slicing
slice_array3 = given_list[-4: -1]
print(f"\n The third slicing is {slice_array3}")

# end of the program

