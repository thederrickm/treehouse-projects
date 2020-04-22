"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def reset_attempts():
    return 0 

def get_random_num():
    return random.randint(1,10) 

def game_menu():
    while True:
        try:
            choice = str(input("Press (R) to resume the game or (Q) to quit game:  "))
        except:
            print(choice)
        else:
            print(choice)


def start_game():
    print("""
------------------------------------
Welcome to the number guessing game!
------------------------------------

""")
    high_score = 11
    random_num = get_random_num()
    attempt = reset_attempts()
    while True:
        try:
            user_guess = int(input("Please guess a number between 1-10, or 0 for menu:  "))
        except NameError:
            print("""That's not a number, try again.
            """)
        else:
            if user_guess >= 1 and user_guess <= 10:
                attempt += 1 
                if user_guess == random_num:
                    print("""Congrats, you solved the riddle in {} attempts!
                    """.format(attempt))
                    if attempt < high_score:
                        high_score = attempt
                        print("You've solved in {} tries. High score is {}".format(attempt, high_score))
                    else:
                        print("You've solved in {} tries. High score is {}.".format(attempt, high_score))
                    # High score logic goes here
                    attempt = reset_attempts()
                    random_num = get_random_num()
                elif user_guess > random_num:
                    print("""Good guess, try something lower.
                    """)
                elif user_guess < random_num:
                    print("""Good guess, try something higher.
                    """)
            elif user_guess == 0:
                game_menu() 
            else:
                print("""Number must be between 1-10!
                """)
                continue


"""Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()

