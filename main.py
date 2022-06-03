import random
import maskpass #To hide the option chosen by the player This can help a lot better when there are 2 players playing the game
Welcome = """
************************************************************
*                                                          *
*     Welcome to the Zeus Rock, Paper, Scissors Game!      *
*                                                          *
************************************************************
"""
print(Welcome)
print("Rules...")
print("If you and the CPU choose the same “Option” it’s a tie, and the game repeats")
print("Rock Smashes Scissors")
print("Paper covers Rock")
print("Scissors cuts Paper \n")
options = ["R", "P", "S"]

while True:
    CPU_choice = random.choice(options)
    print("The CPU has chosen...\n")

    user_entry = maskpass.askpass(prompt="Choose your own option (R for Rock, S for Scissors, P for Paper): ", mask="*")
    #Replaces the user's choice with a *
    user_choice = user_entry.upper()
    if user_choice not in options:
        print(f"The letter {user_choice} is not valid. You can only type either R, P or S")
        
    if user_choice == CPU_choice:
        print("You and the CPU selected the same option. It's a tie!")
    elif user_choice == "R":
        if CPU_choice == "S":
            print("Player(Rock) : CPU(Scissors) \n ***Rock smashes Scissors! You win!***")
        else:
            print("Player(Rock) : CPU(Paper) \n ***Paper covers Rock! You lose.***")
    elif user_choice == "P":
        if CPU_choice == "R":
            print("Player(Paper) : CPU(Rock) \n ***Paper covers Rock! You win!***")
        else:
            print("Player(Paper) : CPU(Scissors) \n ***Scissors cuts Paper! You lose.***")
    elif user_choice == "S":
        if CPU_choice == "P":
            print("Player(Scissors) : CPU(Paper) \n ***Scissors cuts Paper! You win!***")
        else:
            print("Player(Scissors) : CPU(Rock) l\n ***Rock smashes Scissors! You lose.***")

    play_again = input("\nType Y to Play again, or any other button to quit the game: ")
    if play_again.lower() != "y":
        break
