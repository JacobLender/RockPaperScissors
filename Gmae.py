import random

def Menu():     #This is a Function. It will be used here to print menu and decide what choice to pick
    PlayerChoice = 0
    print("Menu\n1. Human Vs Human\n2. Human vs Computer\n3. Exit")

    while PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
        PlayerChoice = int(input("Please choose a game mode: (1,2,3)"))

    if PlayerChoice == 1:
        PvPGame()
    elif PlayerChoice == 2:
        PvCGame()
    else:
        return

def PlayAgain(GameMode):            #When game ends this function is called to see if player feels like playing more
    PlayAgainAnswer = input("Would you like to play again? (Y/N)").capitalize()

    if(PlayAgainAnswer == "Y" and GameMode == "PvP"):
        PvPGame()
    elif(PlayAgainAnswer == "Y" and GameMode == "PvC"):
        PvCGame()
    else:

        print("Alright Whatever. Taking you back to menu.\n")
        print(Menu())


def WinnerDecider(PlayerOne, PlayerTwo):    #Decides who won the Rock Paper Scissor Game
    if PlayerOne == "Rock":
        if PlayerTwo == "Rock":
            Winner = "Draw"
        elif PlayerTwo == "Paper":
            Winner = "PlayerTwo"
        else:
            Winner = "PlayerOne"
    elif (PlayerOne == "Paper"):
        if PlayerTwo == "Paper":
            Winner = "Draw"
        elif PlayerTwo == "Scissor":
            Winner = "PlayerTwo"
        else:
            Winner = "PlayerOne"
    else:
        if PlayerTwo == "Scissor":
            Winner = "Draw"
        elif PlayerTwo == "Rock":
            Winner = "PlayerTwo"
        else:
            Winner = "PlayerOne"

    return Winner

def PvPGame():              #Rules for the Player vs Player Game
    GameMode = "PvP"
    RPS = ["Rock", "Paper", "Scissor"]
    PlayerOne = 999
    PlayerTwo = 999

    while PlayerOne != RPS[0] and PlayerOne != RPS[1] and PlayerOne != RPS[2]:
        PlayerOne = input("Player One, Rock, Paper, or Scissor?").capitalize()

    while PlayerTwo != RPS[0] and PlayerTwo != RPS[1] and PlayerTwo != RPS[2]:
        PlayerTwo = input("Player Two, Rock, Paper, or Scissor?").capitalize()

    Winner = WinnerDecider(PlayerOne, PlayerTwo)

    if Winner == "Draw":
        print("There has been a draw!")
        PlayAgain(GameMode)
    else:
        print(Winner, "is the big daddy grandmaster champion\n")
        PlayAgain(GameMode)

def PvCGame():                 #Player vs Computer Game. Notice the differeneces between the PvP Game and this function
    GameMode = "PvC"
    RPS = ["Rock", "Paper", "Scissor"]
    PlayerOne = 999
    PlayerTwo = 999
    while PlayerOne != RPS[0] and PlayerOne != RPS[1] and PlayerOne != RPS[2]:
        PlayerOne = input("Player One, Rock, Paper, or Scissor?").capitalize()

    PlayerTwo = RPS[int(random.uniform(1,3))]

    Winner = WinnerDecider(PlayerOne, PlayerTwo)
    print("The Computer chose", PlayerTwo, "\n")

    if Winner == "Draw":
        print("There has been a draw!")
        PlayAgain(GameMode)
    else:
        print(Winner, "is the big daddy grandmaster champion\n")
        PlayAgain(GameMode)

def main():        #This is my main. This is where I use the functions I wrote above. I start with call to menu function
    Menu()

main()          #This is my call to function main().
