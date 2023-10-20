"""
Chapter 1 : Exercise I : Count Seconds

Writing a program that calculates the number of seconds in a day.

Prompt the user to enter the number of days, convert days to hours, hours to minutes, minutes to seconds

"""

# start of the program

# printing the program heading
print("\t Seconds Counter")

# asking the user to enter the number of days
days = int(input("\n Please enter the number of days = "))

# converting the days into hrs
hrs = days * 24

# printing the hours
print(f"\n The {days} days make {hrs} hours.")

# converting the hours to minutes
mins = hrs * 60

# printing the minutes
print(f"\n The {days} days make {hrs} hours, and they make {mins} minutes.")

# converting the minutes into seconds
secs = mins * 60

# printing the seconds
print(f"\n The {days} days make {hrs} hours, they make {mins} minutes, and finally all of it makes {secs} seconds.")