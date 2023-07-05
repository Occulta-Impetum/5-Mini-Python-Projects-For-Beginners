import random

# Global Variables
GAME_TITLE = "Number Guesser"
LOWER_BOUND = 1
UPPER_BOUND = 10

#Functions
def hello_player():
    print(f"Welcome to my {GAME_TITLE}!")
    answer = input("Would you like to play a game? ")

    if answer.lower() != "yes":
        print(f"Expected \"yes\", received \"{answer}\".\nGoodbye")
        quit()

    print("Okay! Let's play!")

def check_if_number_and_positive(number):
    if number.isdigit():#checks if the value given is a digit
            number = int(number)#changes the string to an integer
            if number > 0:#checks if the given value is greater than 0
                return number
            else:
                print("Enter a number greater than 0 next time.")
                quit()
    else:
            print("Please enter a number next time.")
            quit()
            

#Main Script
def main():
    secret_number = random.randrange(LOWER_BOUND, UPPER_BOUND + 1)#if you want 1-10 then you have to put 11 as the upper limit because it will never be chosen
    
    print(f"I have generated a secret number between {LOWER_BOUND} and {UPPER_BOUND}.")
    
    guesses = 0
    player_guess = None
    
    while player_guess != secret_number:
        player_guess = input("What is your guess? ")
        
        if player_guess.isdigit():#checks if the value given is a digit
            player_guess = int(player_guess)#changes the string to an integer
            if LOWER_BOUND <= player_guess <= UPPER_BOUND:#checks if the given value is between the UPPER and LOWER bounds
                if player_guess != secret_number:
                    print("Incorrect.")
                    if player_guess < secret_number:
                        print(f"The screcret number is greater than {player_guess}.")
                    else:
                        print(f"The screcret number is less than {player_guess}.")
                guesses += 1
            else:
                print(f"Guess must be between {LOWER_BOUND} and {UPPER_BOUND}.")
        else:
            print("Please enter a number.")
        
    
    print(f"The correct answer was {secret_number}!")
    print(f"It took you {guesses} guesses to get the right answer!")

#Allows calling functions from other scripts wihtout running code
if __name__ == "__main__":
    hello_player()
    
    print(f"The current range is {LOWER_BOUND} - {UPPER_BOUND}.")
    change_range = input("Would you like to change this?")
    
    if change_range.lower() == "yes":
        new_upper_bound = input("What is your large number? ")
        UPPER_BOUND = check_if_number_and_positive(new_upper_bound)
    
    main()

#Sample of pulling in arguments from the command line if needed
""" if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a source and target directory - only.")
    
    source, target = args[1:]
    main(source, target) """