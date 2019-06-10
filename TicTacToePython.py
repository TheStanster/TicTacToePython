# User interaction and viewcode for the Tic-Tac-Toe application

import TTTGameClass # imports the game class

# New object of the game class
TTTGame = TTTGameClass.TicTacToeGame() 
# Create an empty board
board = [' '] * 10

# Prints logo, example grid and a short game description
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
    print("Your goal is to beat the opposing user in getting three of your marks(x/o) in a row on the board.") 
    print("An example of the board is shown above. The numbers represent the possible positions in which you can place your mark.")
    print("Take a good look at what numbers correspond to which positions.\nShould you forget, you can scroll up to the example or check the numpad on the right side of your keyboard.\n")

# Starts a single round of Tic-Tac-Toe and runs until the round is finished
def playGame():
    
    TTTGame.Reset()
    ResetBoard()
    takeTurns()

    # After the round results in a win or draw
    presentGameSummary()
    askToPlayAgain()
    

    return   

# Lets the users take turns until the game is either won or ends in a draw
def takeTurns():
    while TTTGame.bGameIsWon == False and TTTGame.bGameIsDraw == False:
        TTTGame.NextTurn()
        turn = str(TTTGame.currentTurn)
        print("\nTurn " + turn + ".\n")
        submitChoice()
        TTTGame.GetBoard(board)
        TTTGame.BoardCheck(board, TTTGame.currentMark)
        
# Asks for user input until a valid value is supplied, then submits it to the board
def submitChoice():
    TTTGame.GetCurrentPlayerMark()
    TTTGame.GetCurrentPlayerNumber()

    try:    # makes sure input is an integer
        choice = input("Player " + TTTGame.playerNum + " please enter the number corresponding to the position on the board where you want to place your mark. \n")
        choice = int(choice)
        if board[choice] == TTTGame.userOneMark or board[choice] == TTTGame.userTwoMark:
            print("This position has already been chosen. Please enter an empty position on the board. \n")
            return submitChoice() 
        elif choice >= 1 and choice <= 9:
            TTTGame.place_mark(board, TTTGame.currentMark, choice)
        else:   #To catch those pesky zeros
            print("Please enter a number between 1 and 9. \n")
            return submitChoice()
    except:
        print("Please enter a number between 1 and 9. \n")
        return submitChoice()

# Ask if user wants to play before start of first game
def askToPlayGame():
        
    answer = input("Would you like to play a game of tic-tac-toe? (y/n) \n").lower()
    print('\n')
    if (answer == 'yes' or answer == 'y'):
        print("Player 1 will be represented on the board by an " + TTTGame.userOneMark + " mark.")
        print("Player 2 will be represented on the board by an " + TTTGame.userTwoMark + " mark. \n")
        return 
    elif (answer == 'no' or answer == 'n'):
        answer = ''
        answer = input("Are you sure? (y/n) \n").lower()
        print('\n')
        if (answer == 'yes' or answer == 'y'):
            print("Have a nice day!")
            return exit ()
        else:
            return askToPlayGame()
    else:
        print("I didn't quite get that.\n")
        return askToPlayGame()
               
# Ask whether the user wants to play again when a round has finished
def askToPlayAgain():
    
    answer = input("Would you like to play another round? (y/n) \n").lower()
    print('\n')
    if (answer == 'yes' or answer == 'y'):
        return playGame() 
    elif (answer == 'no' or answer == 'n'):
        answer = ''
        answer = input("Are you sure? (y/n) \n").lower()
        print('\n')
        if (answer == 'yes' or answer == 'y'):
            print("Have a nice day!")
            return exit ()
        else:
            return askToPlayAgain()
    else:
        print("I didn't quite get that.\n")
        return askToPlayAgain()
              
# Clears the board, so that values entered onto the board do not carry over to succesive rounds
def ResetBoard():
    board[1]= ' '
    board[2]= ' '
    board[3]= ' '
    board[4]= ' '
    board[5]= ' '
    board[6]= ' '
    board[7]= ' '
    board[8]= ' '
    board[9]= ' '
    
# Informs the user that the round is finished 
# Also presents whether there was a draw or a win, and if applicable, who won in how many turns
def presentGameSummary():
    if TTTGame.bGameIsDraw == True:
        print("That's a draw!")
        print("It seems that you were evenly matched.")
    elif TTTGame.bGameIsWon == True:
        print("Congratulations!")
        print("Player " + TTTGame.playerNum + " managed to beat their opponent in " + str(TTTGame.currentTurn) + " turns.")
        print("\n")
    else:
        print("The game was was neither lost nor was it a draw.")
        print("How did you even get here?")

# Entry point for application
def main():		
	
    intro()
    askToPlayGame()
    playGame()
    
    return 0		# Exit application

if __name__ == "__main__": main()
   