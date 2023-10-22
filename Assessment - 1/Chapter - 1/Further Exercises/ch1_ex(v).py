"""
Chapter 1 : Exercise V : Lambda Function

Writing a program that uses lambda function in the function sort the list elements of the tuple based 
on marks low to high and high to low. The list is given as:

marks = [("CodeLab I",67),("web Development", 75),("CodeLabII",74),("Smartphone Apps",68),("Games Development",70),
("Responsive web",65)]

"""

# start of the progam

# creating the given list of tuples
marks = [("CodeLab I",67),("web Development", 75),("CodeLabII",74),("Smartphone Apps",68),("Games Development",70),
         ("Responsive web",65)]


# first printing the original list
print(f"\n The original list: \n {marks}")


# creating a lambda function with the sort function (this sorts the list in ascending order)
# here, the parameter key lambda is passed, and since the order should be based on marks, the index pos. of the marks in
# tuples is 1, so we have written x:x[1]
marks.sort(key = lambda x:x[1])

# printing the list in ascending order
print(f"\n The list in the alphabetical order is \n {marks}")

# now creating the lambda function with the sort function to display the list in descending order
# for reversing, we just set reverse = True
marks.sort(key = lambda x:x[1], reverse = True)

# printing the result in descending order
print(f"\n The list in descending order is \n {marks}")

# end of the program (NOT DONE YET)