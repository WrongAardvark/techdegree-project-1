import random

def start_game():
    print("Welcome to the Rando-Numbo!")
    print("In this game, I will pick a number between 1 and 10, and you will try to guess the number in the least amount of guesses possible.")
    guess_amount = 0
    play_game = True
    high_score = []
    player_guess = None
    
    while play_game:
        random_num = random.randint(1,10)
        
        try:
            while player_guess != random_num:
                
                temp_player_guess = input("I picked a number between 1 and 10. Try to guess:  ")
                player_guess = int(temp_player_guess)
            
                if player_guess > 10 or player_guess < 1:
                    raise ValueError("Use a number that doesn't exceed the range:  ")
                    continue
                
                elif player_guess < random_num:
                    print("")
                    print("Your number was too low, try again:  ")
                    guess_amount += 1
                    continue
                    
                elif player_guess > random_num:
                    print("")
                    print("Your number was too high, try again:  ") 
                    guess_amount += 1
                    continue
                          
                else:
                    guess_amount += 1
                    if player_guess == random_num:
                        print("You got it! The number was {}!".format(random_num))
                        print("It took you {} guesses.".format(guess_amount))
                        high_score.append(guess_amount)
                        break
                    
        except ValueError as ve:
            if "invalid" in str(ve):
                print("ValueError: Please use an integer:  ")
                
            else:
                print("Out of range. Please try again.")
            continue
            
        keep_playing = input("Would you like to play again? (yes/no):  ")
        
        if keep_playing.lower() == "yes":
            guess_amount = 0
            print("")
            print("{} is your current high score. Try to beat it!".format(min(high_score)))
            continue
        elif keep_playing.lower() != "yes":
            print("Your lowest number of guesses was {}.".format(min(high_score)))
            
            print("Thank you for playing!")
            play_game = False
            break

start_game()  