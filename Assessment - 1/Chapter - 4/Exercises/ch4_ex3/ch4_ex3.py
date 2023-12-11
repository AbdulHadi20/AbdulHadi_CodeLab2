"""
Chapter 4 : Exercise 3 : Reading to a list

The file numbers.txt has a list of 100 integer numbers each on a newline. 
Create a python program that puts this data into a list, then output the values in integer format.

"""

with open('numbers.txt', 'w') as file:
    num_list = []
    for line in file:
        num = int(line)
        num_list.append(num)

    print(num_list)