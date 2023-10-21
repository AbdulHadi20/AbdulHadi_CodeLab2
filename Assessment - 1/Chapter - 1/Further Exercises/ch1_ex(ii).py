"""
Chapter 1 : Exercise II : Sum of Digits in a Number

Writing a  program that prints the sum of digits in a number.
Ex : If user enter 46594, so result should be 4 + 6 + 5 + 9 + 4 = 28

"""

# start of the program

# creating a list to store user entries
numlist = []

# creating a loop asking the user to enter a value
while True:
    # asking the user to enter a number
    num = int(input("\n Please enter any random number = "))
    # adding the number in the list
    numlist.append(num)

    more = input("\n Do you wish to add more values (y/n) = ")

    if more == 'y':
        continue

    elif more == 'n':
        break

    else:
        print("\n ERROR. TRY AGAIN")
        continue

# now, adding all the elements in the list
sum = 0
for i in numlist:
    sum = sum + i

print(f"\n The sum of all the numbers, {numlist} is {sum}")

# end of the program