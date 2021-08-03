import random


def start_game():
    print("Welcome to the Rando-Numbo!")
    print("In this game, I will pick a number between 1 and 10, and you will try to guess the number in the least amount of guesses possible.")
    guess_amount = 0
    play_game = True
    high_score = []
    
    while play_game:
        random_num = random.randrange(1,11)
        
        try:
            player_guess = int(input("I picked a number between 1 and 10. Try to guess:  "))
        except ValueError:
            print("")
            print("Make sure you use an integer, not a letter or word.")
            continue
        
                
                
            
        while player_guess != random_num:
            
             
            try:
                int(player_guess) == False
            except ValueError:
                print("")
                player_guess = input("ValueError: Please use an integer:  ")
            
               
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
                    print("Your lowest number of guesses was {}.".format(min(high_score)))
                    #looked up min() for high score. found on https://computersciencehub.io/python/python-find-smallest-number-in-list/
                    
                    print("Thank you for playing!")
                    play_game = False
                    break
    
# Kick off the program by calling the start_game function.
start_game()                
