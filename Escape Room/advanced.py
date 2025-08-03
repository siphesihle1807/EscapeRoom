def advanced_level():
    player_lives = 3
    print("Advanced Level: You’re inside a futuristic lab sealed by AI.")

    # Stage 1 of the advanced level.
    while True:
        choice = input(
            "\nThe AI says: 'Solve the riddle or face the consequence.'\n"
            "'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?'\n"
            "1. An echo.\n"
            "2. A shadow.\n"
            "3. A dream.\n"
            "Your answer: "
        )
        if choice == "1":
            print("Correct! The AI grants you access to the next room.")
            break
        elif choice in ["2", "3"]:
            player_lives -= 1
            print(f"Wrong! You lose a life. Lives left: {player_lives}")
            if player_lives == 0:
                print("AI security neutralized you. Game over!")
                return
        else:
            print("Invalid input. Try again.")

    # Stage 2 of the advanced level.
    while True:
        choice = input(
            "\nYou're in a control room with two buttons:\n"
            "1. Press the red button.\n"
            "2. Press the blue button.\n"
            "Your choice: "
        )
        if choice == "2":
            print("The system shuts down. A secret door opens!")
            break
        elif choice == "1":
            player_lives -= 1
            print(f"An alarm sounds! You lose a life. Lives left: {player_lives}")
            if player_lives == 0:
                print("Security bots apprehend you. Game over!")
                return
        else:
            print("Invalid input. Try again.")

    print("\nYou escape the lab just in time. You've conquered the Advanced Level!")
    replay = input("Would you like to play again? (yes/no): ").lower()
    if replay == "yes":
        advanced_level()
