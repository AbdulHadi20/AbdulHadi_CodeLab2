"""
Chapter 1 : Exercise IV : Count Items

Writing a program that counts the amount of times an element has appeared on the list.
The list is given below:

staff = ["Arshiya", "Usman", "Iftikhar", "Usman","Rafia", "Mary", "Anmol","Zainab","Iftikhar", "Arshiya","Rafia","Jake"]

"""

# start of the program

# creating a list 
staff = ["Arshiya", "Usman", "Iftikhar", "Usman","Rafia", "Mary", "Anmol","Zainab","Iftikhar", "Arshiya","Rafia","Jake"]

# creating a dictionary, where we set the key as i, and its value as zero
# added a for loop to go through the complete list
staff_dict = {i:0 for i in staff}

# created another for loop to count the items, and then, incrementing the values if the keys are repeated
for i in staff:
    staff_dict[i] += 1

# printing the output
print(f"\n The dictionary is displayed below: \n {staff_dict}")

# end of the program 