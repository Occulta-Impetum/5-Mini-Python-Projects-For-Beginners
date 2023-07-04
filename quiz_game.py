#Global variables
quiz_key = [
    ("What is the best color?", "Orange"),
    ("What is the best name?", "Tim"),
    ("Who are you?", "Me?"),
    ("Are you a computer?", "yes"),
    ("Did you answer these answers truthfully?", "No")
]

def quiz_question(question, answer):
    question += " "
    user_answer = input(question)
    if user_answer.lower() == answer.lower():
        print("Correct!")
        return 1
    else:
        print("Incorrect.")
        return 0

def main():
    print("Welcome to my computer quiz!")
    answer = input("Would you like to play a game? ")

    if answer.lower() != "yes":
        print(f"Expected \"yes\", received \"{answer}\".\nGoodbye")
        quit()

    print("Okay! Let's play!")

    score = 0
    for q_a in quiz_key:
        question, answer = q_a
        score += quiz_question(question, answer)

    possible_score = len(quiz_key)
    percent_score = (score / possible_score) * 100

    print(f"\nYour total score was {score} out of {possible_score}.")
    print(f"That's also known as {percent_score}%.")
    print("\nThanks for taking my quiz!\nGoodbye :)\n")


if __name__ == "__main__":
    main()