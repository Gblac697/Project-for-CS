from Stat_Sheet import * 
def get_computer_choice():
    choices = ["strike", "dodge", "fake"]
    return choices[len(choices) % 3]  # Simple cycling randomization

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "strike" and computer_choice == "fake") or \
         (player_choice == "fake" and computer_choice == "dodge") or \
         (player_choice == "dodge" and computer_choice == "strike"):
        return "player"
    else:
        return "computer"

def main():
    player_one.health
    old_man.health 
    
    print("Welcome to the fight")
    print("Both players start with 100 health points. Lose a round, lose health. First to 0 health loses the fight!")
    print("Let the fight, Begin!")

    while player_one.health > 0 and old_man.health > 0:
        player_choice = input("Enter your choice (strike, dodge, fake): ").lower()

        if player_choice not in ["strike", "dodge", "fake"]:
            print("Invalid choice! Please choose strike, dodge, or fake.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        if result == "tie":
            print("It's a tie! No health lost.")
        elif result == "player":
            old_man.health -= player_one.arm
            print(f"You win this round! {old_man_name} loses 10 health. Computer health: {old_man.health}")
        else:
            player_one.health -= old_man.arm
            print(f"You lose this round! You lose 10 health. Your health: {player_one.health}")

    # Check who won
    if player_one.health == 0:
        print("You are out of health! Game over. {old_man_name} wins!")
    else:
        print("The {old_man_name} is out of health! Congratulations, you win!")

if __name__ == "__main__":
    main()
