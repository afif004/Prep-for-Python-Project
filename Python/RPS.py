import random
def get_choices():
    player_choice = input("Enter Rock/Paper/Scissors\n")
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "comp": computer_choice}
    return choices
def check_win(player, comp):
    print("You chose " + player + ", computer chose " + comp)
    if(player==comp):
        return "Its a Tie!"
    elif(player == "Rock"):
        if comp == "Scissors":
            return "Rock smashes Scissors! You Win!"
        else:
            return "Paper covers Rock! You lose."
    elif(player == "Paper"):
        if (comp == "Scissors"):
            return "Scissors cuts Paper! You lose."
        else:
            return "Paper covers Rock! You win!"
    else:
        if (comp == "Rock"):
            return "Rock smashes Scissors! You lose."
        else:
            return "Scissors cuts Paper! You win!"
choices = get_choices()
print(check_win(choices["player"], choices["comp"]))
