# a simple rock - paper - siscors game
# importing a module "random" from the Python library
import random

# creating a list for the computer and the user
choices = ['rock', 'paper', 'siscors']

# welcoming the user to the game
print("Welcome to the rock - paper - siscors game !!!")

# creating a while loop, so that the code keeps running until a certain codition is met
while True:
  # printing the list of choices
  print(choices)

  # saving the users choice in a variable
  user_input = input("Please enter your choice : ")

  # generating a random move for the computer
  comp_choice = random.choice(choices)

  # displaying both of the choices, the user's and the computer's
  print("You chose", user_input + "\n The computer chose", comp_choice)

  # setting condition to see if the user's choice is in the list, runs if true
  if user_input in choices:

    # setting a condition if both players choose the same
    if user_input == comp_choice: 
      print("You both chose ", user_input)
      print("It is a tie !")

    # setting the res of the conditions, based on the players' choices
    elif user_input == 'rock' and comp_choice == 'paper':
      print("You chose", choices[0], " and the computer chose", choices[1])
      print("You loose ! \n Computer wins !")

    elif user_input == 'paper' and comp_choice == 'rock':
      print("You chose", choices[1], " and the computer chose", choices[0])
      print("You win ! \n Computer lost !")

    elif user_input == 'rock' and comp_choice == 'siscors':
      print("You chose", choices[0], " and the computer chose", choices[2])
      print("You win ! \n Computer lost !")
      
    elif user_input == 'siscors' and comp_choice == 'rock':
      print("You chose", choices[2], " and the computer chose", choices[1])
      print("You loose ! \n Computer wins !")
      
    elif user_input == 'paper' and comp_choice == 'siscors':
      print("You chose", choices[1], " and the computer chose", choices[2])
      print("You loose ! \n Computer wins !")

    elif user_input == 'siscors' and comp_choice == 'paper':
      print("You chose", choices[2], " and the computer chose", choices[1])
      print("You win ! \n Computer lost !")

  # runs if the users selects 'q'     
  elif user_input == 'q':
    print("You quit ! Thankyou for playing")
    break # ends the loopsss

  # runs if the user enters any other value that is not in the list
  else:
    print("Invalid Entry ! Please try again")


    