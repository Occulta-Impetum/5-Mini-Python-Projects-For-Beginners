# This is interesting but nesting these if statements get's tedius real quick
# It would be interesting to use match cases and load in the rooms/locations stored as separate variables/dictionaries

""" Design a system that scales elegantly.
Your game engine can be very simple and clean, and the whole state machine and branching can be defined in data.
Something like a json file with rooms, each room has a prompt and valid actions.
Those actions can move you to a new room, print something, or set flags.
You can even set prerequisites on certain actions, so that you need a blue key to open the blue door...
But definitely split your data and game engine. """

# Global Variables



#Functions


#Main Script
def main():
    name = input("Type your name: ")
    print(f"Welcome {name} to this adventure!")
    
    answer = input("You find yourself on a dirt road that has come to a fork. Would you like to go right or left? ").lower()
    if answer == "right":
        answer = input("You come to a bridge that is crossing a small stream. Type bridge to go over the bridge or swim to swim across the river:  ").lower()
        
        if answer == "bridge":
            print()
        elif answer == "swim":
            print()
        else:
            print("That was not a valid choice. You loose.")
        
    elif answer == "left":
        print()
    else:
        print("That was not a valid choice. You loose.")

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