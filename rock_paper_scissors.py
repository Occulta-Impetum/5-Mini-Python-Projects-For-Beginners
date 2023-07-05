import random

# Global Variables
OPTIONS = ["rock", "paper", "scissors"]

#Functions


#Main Script
def main():
    user_wins = 0
    computer_wins = 0
    
    while True:
        user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
        
        if user_input == "q":
            break
        
        if user_input not in OPTIONS:
            continue
    
        random_number = random.randint(0,2)
        # rock: 0, paper: 1, scissors: 2
        computer_pick = OPTIONS[random_number]
        
        print(f"I picked {computer_pick}.")
        
        if user_input == "rock" and computer_pick == "scissors":
            print("You won!")
            user_wins += 1
        elif user_input == "paper" and computer_pick == "rock":
            print("You won!")
            user_wins += 1
        elif user_input == "scissors" and computer_pick == "paper":
            print("You won!")
            user_wins += 1
        elif user_input == computer_pick:
            print("TIE!")
        else:
            print("You lost.")
            computer_wins += 1
    
    print("\nThe final score was!")
    print(f"You: {user_wins}")
    print(f"Computer: {computer_wins}")
    
    if user_wins > computer_wins:
        print("\nYOU WON!!!\n")
    elif user_wins < computer_wins:
        print("\nI WON!!!\nMWA HA HA HA HA HA HA HA...\n**clears throat**\nSorry, better luck next time :)\n")
    else:
        print("\nI WON!\n ...wait\nA tie?\nThat's not right...\n\n")
        print("The final score was!")
        print(f"You: {user_wins-1}")
        print(f"Computer: {computer_wins}\n")
    
    print("Goodbye")

#Allows calling functions from other scripts wihtout running code
if __name__ == "__main__":
    main()

#Sample of pulling in arguments from the command line if needed
""" if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a source and target directory - only.")
    
    source, target = args[1:]
    main(source, target) """