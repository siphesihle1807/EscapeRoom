def intermediate_level():
    player_lives = 3
    print("Intermediate Level: You enter an old library with creaking floors.")

    # Stage 1 of the intermediate level.
    while True:
        choice = input(
            "\nYou see a dusty bookshelf and a suspicious floor tile.\n"
            "1. Pull a book titled 'The Secret Passage'.\n"
            "2. Step on the suspicious tile.\n"
            "3. Sit and wait.\n"
            "Your choice: "
        )
        if choice == "1":
            print("A hidden passage opens behind the shelf. Nice move!")
            break
        elif choice in ["2", "3"]:
            player_lives -= 1
            print(f"Trap triggered! You lose a life. Lives left: {player_lives}")
            if player_lives == 0:
                print("You were caught by the trap. Game over!")
                return
        else:
            print("Invalid input. Try again.")

    # Second stage of the game.
    while True:
        choice = input(
            "\nThe passage leads to a room with two artifacts:\n"
            "1. Touch the glowing orb.\n"
            "2. Open the mysterious ancient box.\n"
            "Your choice: "
        )
        if choice == "2":
            print("The box contains a key and a map! You're getting closer.")
            break
        elif choice == "1":
            player_lives -= 1
            print(f"The orb zaps you! You lose a life. Lives left: {player_lives}")
            if player_lives == 0:
                print("The orb's power overwhelms you. Game over!")
                return
        else:
            print("Invalid input. Try again.")

    print("\nYou use the map and the key to escape the library. Congratulations!")
    replay = input("Would you like to play again? (yes/no): ").lower()
    if replay == "yes":
        intermediate_level()
