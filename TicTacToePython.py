# User interaction and viewcode for the Tic-Tac-Toe application

import TTTGameClass # imports the game class


TTTGame = TTTGameClass.TicTacToeGame() # New object of the game class


def intro():
    print("    SSS   V     V")
    print("  S    S  V     V  7 | 8 | 9")
    print("  S       V     V -----------")
    print("    SSS   V     V  4 | 5 | 6")
    print("       S  V     V -----------")
    print("  S    S   V   V   1 | 2 | 3")
    print("    SSS      V   ")
    print("\n")     #short game description
    print("Welcome to SVTTT (Stan Valster's Tic-Tac-Toe), a game of shapes.")
    print("\n")
    print("Your goal is to beat the opposing user in getting three of your marks(x/o) in a row on the grid.") # TODO make this and the next line appear after a few moments
    print("An example of the grid is shown above. The numbers represent the possible positions in which you can place your mark.\n") # Prints logo, example grid and a short game description


def playGame():

    TTTGame.Reset()
    TTTGame.GetBoard
    print('Hot diggity\n')
    return # Starts a single round of Tic-Tac-Toe


def askToPlayGame():

    answer = ''
    while (answer == ''):
        answer = input("Would you like to play a game of tic-tac-toe? (y/n) \n")
        print('\n')
        if (answer == 'yes' or answer == 'y'):
            return  
        elif (answer == 'no' or answer == 'n'):
            answer = ''
            answer = input("Are you sure? (y/n) \n")
            print('\n')
            if (answer == 'yes' or answer == 'y'):
                print("Have a nice day!")
                return exit ()
            else:
                return askToPlayGame()
        else:
            print("I didn't quite get that.\n")
            return askToPlayGame() # Ask if user wants to play before start of first game


def askToPlayAgain():
    
    answer = ''
    while (answer == ''):
        answer = input("Would you like to play another round? (y/n) \n")
        print('\n')
        if (answer == 'yes' or answer == 'y'):
            return  
        elif (answer == 'no' or answer == 'n'):
            answer = ''
            answer = input("Are you sure? (y/n) \n")
            print('\n')
            if (answer == 'yes' or answer == 'y'):
                print("Have a nice day!")
                return exit ()
            else:
                return askToPlayAgain()
        else:
            print("I didn't quite get that.\n")
            return askToPlayAgain()
    return # Ask whether the user wants to play again when a round has finished


def presentGameSummary():

    return


def main():		# Entry point for application
	
    intro()
    askToPlayGame()
    playGame()
    #presentGameSummary()
    askToPlayAgain()
    
    return 0		# Exit application

if __name__ == "__main__": main()
   