"""
Chapter 1 : Exercise 11 : Year Tuples

Writing a program that creates a tuple consisting of random years, preferably:
tuple =(2017,2003,2011,2005,1987,2009,2020,2018,2009)

Then performing the following operations with the tuple:

- Access the value at index 3
- Reverse the tuple and print the original tuple and reversed tuple
- Count the nuumber of times 2009 is in the tuple (use count() method)
- Get the index value of 2018 (use index method)
- Find the length of the given tuple (use len() method)
"""

# start of the program

# creating a tuple
years = (2017,2003,2011,2005,1987,2009,2020,2018,2009)

#accessing the value at index 3
print(f"\n The value in the tuple at index 3 is {years[3]}")

# printing the orignial tuple and the reversed tuple
print(f"\n The original tuple is: {years}")
print(f"\n The reversed tuple is {years[::-1]}")

# counting the number of times 2009 is in the tuple
print(f"\n The year 2009 appears in the tuple {years.count(2009)} times.")

# finding the index value of the year 2018
print(f"\n The index value of the year 2018 is {years.index(2018)}.")

# finding the length of the tuple
print(f"\n The length of the tuple is {len(years)}")

# end of the program

