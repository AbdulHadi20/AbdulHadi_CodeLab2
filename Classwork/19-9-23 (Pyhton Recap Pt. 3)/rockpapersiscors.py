# welcoming the user to the game
print("\t Welcome to the Rock - Paper - Siscors Game !!!")

# creating a list for the computer to make a move
moves = ['Rock', 'Paper', 'Siscors']

# creating a function for the computer to make a move
def comp_move():
    import random

    computersmove = random.move(moves)
    print("The computer played ", computersmove)

while True:
    user_move = int(input(print("Select the move you want to make = \n 1. Rock \n 2. Paper \n 3. Siscors \n ")))
    if user_move == 1:
        print("You chose to play Rock!")
        comp_move()
        
        if user_move == 1 and comp_move() == moves[1]:
            print("You lost!")
            
        elif user_move == 1 and comp_move() == moves[0]:
            print("It's a tie!")
            
        elif user_move == 1 and comp_move() == moves[2]:
            print("You win!")
    
    elif user_move == 2:
        print("You chose to play Paper!")
        comp_move()

        if user_move == 2 and comp_move() == moves[2]:
            print("You lost!")

        elif user_move == 2 and comp_move() == moves[1]:
            print("It's a tie!")

        elif user_move == 2 and comp_move() == moves[0]:
            print("You win!")

    elif user_move == 3:
        print("You chose to play Siscors!")
        comp_move()

        if user_move == 3 and comp_move() == moves[0]:
            print("You lost!")

        elif user_move == 3 and comp_move() == moves[2]:
            print("It's a tie!")
            
        elif user_move == 3 and comp_move() == moves[1]:
            print("You win!")

    else:
        print("Invalid choice!")
