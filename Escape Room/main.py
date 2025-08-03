from beginner import beginner_level
from intermediate import intermediate_level
from advanced import advanced_level

def user_choice():
    while True:
        print("Welcome to Escape Room!")
        player_choice = input(
            "Pick a door, and let the mystery begin!! 😎\n"
            "1. Beginner\n"
            "2. Intermediate\n"
            "3. Advanced\n"
            "Or type: 'End'\n"
            "Your choice: "
        )

        if player_choice == "1":
            print("#############################B-E-G-I-N-N-E-R############################")
            print("You have chosen the beginner level. Let's start!")
            beginner_level()
        elif player_choice == "2":
            print("########################I-N-T-E-R-M-E-D-I-A-T-E############################")
            print("You have chosen the intermediate level. Let's start!")
            intermediate_level()
        elif player_choice == "3":
            print("########################A-D-V-A-N-C-E-D############################")
            print("You have chosen the advanced level. Let's start!")
            advanced_level()
        elif player_choice.lower() == "end":
            print("You have chosen to end the game. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 'End'.")

user_choice()
