def beginner_level():
    player_lives = 3

    print("Level 1: You wake up in the janitor's closet. It's dark. What do you do?")
    while True:
        choice = input(
            "1. Feel around the walls for a light switch.\n"
            "2. Open the nearby cabinet.\n"
            "3. Bang on the door and yell for help.\n"
            "Your choice: "
        )
        if choice == "1":
            print("You find the light switch and reveal the room. Good job!")
            break
        elif choice in ["2", "3"]:
            player_lives -= 1
            print(f"Oops! Wrong choice. You have {player_lives} lives left.")
            if player_lives == 0:
                print("You've run out of lives. Game over!")
                return
        else:
            print("Invalid choice. Try again.")

    print("\nLevel 2: You see a vent and a door. Which way do you go?")
    while True:
        choice = input("1. Crawl through the vent.\n2. Open the door.\nYour choice: ")
        if choice == "1":
            print("The vent is too small. You get stuck and lose a life.")
            player_lives -= 1
            if player_lives == 0:
                print("You're out of lives. Game over!")
                return
        elif choice == "2":
            print("You open the door and escape the janitor's closet. You win Beginner Level!")
            break
        else:
            print("Invalid choice. Try again.")

    replay = input("\nWould you like to play again? (yes/no): ").lower()
    if replay == "yes":
        beginner_level()
