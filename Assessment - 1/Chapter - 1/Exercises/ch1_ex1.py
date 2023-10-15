"""
Chapter 1 : Exercise 1 : User Input Output

Writing a code to prompt the user into entering their age and name, then printing the results on the screen. Finding the 
length of the name and then the potential age of the user, the year after.

"""

# starting of the program

#greeting the user
print("\n Hello User !!!")

#asking the user for their name and age and saving them in variables respectively
user_name = str(input("\n What is your name ? \n "))
user_age = int(input("\n What is your age ? \n "))

# printing a statement to complement seeing the user, using title() function to capitalize the first letter of the name of the user
print("\n It's great to see you, ", user_name.title())

#using len function to count the letters in the name of the user, then displaying the answer to the user
print("\n The length of your name is: ", len(user_name))

#incrementing the user's age by 1 to display the age of the user for next year
age_nxt_yr = user_age + 1
print(f"\n You will be {age_nxt_yr} next year.")

#ending of the program