"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def attempt_rst():
    return 0
    
def game_intro():
    print("""
===================================
Let's play the number guessing game!
===================================
    """)
    return random.randint(1,10)

def start_game():
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
    random_num = game_intro()
    print("""You are the first player, no high score exists!
            """)
    attempt = attempt_rst()
    high_score = 11
    while True:
        response = input("Please enter a number between 1-10:  ")
        try:
            response = int(response)
        except ValueError:
            print("That's not a number!")
        else:
            if response >= 1 and response <= 10:
                attempt += 1
                if response == random_num:
                    if attempt == 1:
                        print("Wow! You won the game in {} attempt!!".format(attempt))
                    else:
                        print("Nice! You guessed correctly in {} attempts".format(attempt))
                    if attempt < high_score:
                        print("""You've set a new high score! High score: {}
                                """.format(attempt))
                        high_score = attempt
                    elif attempt > high_score:
                        print("""High score: {}
                                """.format(high_score))
                    response = input("Would you like to play again? (y/n):  ")
                    response = str(response)
                    if response == 'y':
                        print("Great, lets go!")
                        random_num = game_intro()
                        attempt = attempt_rst()
                        continue
                    elif response == 'n':
                        print("Have a great day! Exiting.")
                        break
                    else:
                        print("Invalid response, exiting game.")
                        break
                elif response > random_num:
                    print("""It's lower.
                           """)
                elif response < random_num:
                    print("""It's higher.
                            """)
            else:
                print("Try again!")




if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()

