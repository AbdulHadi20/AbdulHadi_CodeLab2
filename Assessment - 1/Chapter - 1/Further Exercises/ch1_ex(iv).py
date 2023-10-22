"""
Chapter 1 : Exercise IV : Count Items

Writing a program that counts the amount of times an element has appeared on the list.
The list is given below:

staff = ["Arshiya", "Usman", "Iftikhar", "Usman","Rafia", "Mary", "Anmol","Zainab","Iftikhar", "Arshiya","Rafia","Jake"]

"""

# start of the program

# creating a list 
staff = ["Arshiya", "Usman", "Iftikhar", "Usman","Rafia", "Mary", "Anmol","Zainab","Iftikhar", "Arshiya","Rafia","Jake"]

# displaying the list
print(f"\n The given list is {staff}")

# now, using the count function to count the amount of times an element has appeared in the list
# creating a seperate variable for each name
name1 = staff.count("Arshiya")
name2 = staff.count("Usman")
name3 = staff.count("Iftikhar")
name4 = staff.count("Rafia")
name5 = staff.count("Mary")
name6 = staff.count("Anmol")
name7 = staff.count("Zainab")
name8 = staff.count("Jake")

# printing the results
print(f"\n The name {staff[0]} has appeared {name1} times in the list")
print(f"\n The name {staff[1]} has appeared {name2} times in the list")
print(f"\n The name {staff[2]} has appeared {name3} times in the list")
print(f"\n The name {staff[4]} has appeared {name4} times in the list")
print(f"\n The name {staff[5]} has appeared {name5} times in the list")
print(f"\n The name {staff[6]} has appeared {name6} times in the list")
print(f"\n The name {staff[7]} has appeared {name7} times in the list")
print(f"\n The name {staff[11]} has appeared {name8} times in the list")

# end of the program (TRY ANOTHER WAY)