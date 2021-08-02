"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    print("Welcome to the Rando-Numbo!")
    print("In this game, I will pick a number between 1 and 10, and you will try to guess the number in the least amount of guesses possible.")
    guess_amount = 0
    play_game = True
    high_score = []
    
    while play_game:
        random_num = random.randrange(1,10)
        
        try:
            player_guess = int(input("I picked a number between 1 and 10. Try to guess:  "))
        except ValueError:
            print("Make sure you use an integer, not a word.")
            
        while player_guess != random_num:
            #high_score
            guess_amount += 1
            if int(player_guess) < random_num:
                print("")
                player_guess = input("Your number was too low, try again:  ")
            elif int(player_guess) > random_num:
                print("")
                player_guess = input("Your number was too high, try again:  ")
            elif int(player_guess) == random_num:
                print("You got it! The number was {}!".format(random_num))
                print("It took you {} guesses.".format(guess_amount))
                high_score.append(guess_amount)
                
                
                keep_playing = input("Would you like to play again? (yes/no):  ")
                
                if keep_playing.lower() == "yes":
                    guess_amount = 0
                    break
                elif keep_playing.lower() != "yes":
                    print("Your best score was {}.".format(min(high_score)))
                    #looked up min()function for high score. found on https://computersciencehub.io/python/python-find-smallest-number-in-list/
                    
                    print("Thank you for playing!")
                    play_game = False
                    break
    
                
                
        
        

    
          
          
    
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



# Kick off the program by calling the start_game function.
start_game()