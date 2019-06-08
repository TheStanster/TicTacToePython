# User interaction and viewcode for the Tic-Tac-Toe application

import TTTGameClass # imports the game class


TTTGame = TTTGameClass.TicTacToeGame() # New object of the game class
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
    print("Your goal is to beat the opposing user in getting three of your marks(x/o) in a row on the board.") # TODO make this and the next line appear after a few moments
    print("An example of the board is shown above. The numbers represent the possible positions in which you can place your mark.\n")                        

# Starts a single round of Tic-Tac-Toe
def playGame():
    
    TTTGame.Reset()
    ResetBoard()
    takeTurns()

    # After the round results in a win or draw
    presentGameSummary()
    askToPlayAgain()
    

    return   

def takeTurns():
    while TTTGame.bGameIsWon == False and TTTGame.bGameIsDraw == False:
        TTTGame.NextTurn()
        turn = str(TTTGame.currentTurn)
        print("\nTurn " + turn + ".\n")
        submitChoice()
        TTTGame.GetBoard(board)
        TTTGame.BoardCheck(board, TTTGame.currentMark)
        

def submitChoice():
    TTTGame.GetCurrentPlayerMark()
    TTTGame.GetCurrentPlayerNumber()

    choice = input("Player " + TTTGame.playerNum + " please enter the number corresponding to the position on the board where you want to place your mark. \n")
    choice = int(choice)
    if board[choice] == TTTGame.userOneMark or board[choice] == TTTGame.userTwoMark:
        print("This position has already been chosen. Please enter an empty position on the board. \n")
        return submitChoice() 
    elif choice >= 1 and choice <= 9:
        TTTGame.place_mark(board, TTTGame.currentMark, choice)
    else:
        print("Please enter a number between 1 and 9. \n")
        return submitChoice()


# Ask if user wants to play before start of first game
def askToPlayGame():

    answer = ''
    while (answer == ''):
        answer = input("Would you like to play a game of tic-tac-toe? (y/n) \n")
        print('\n')
        if (answer == 'yes' or answer == 'y'):
            print("Player 1 will be represented on the board by an " + TTTGame.userOneMark + " mark.")
            print("Player 2 will be represented on the board by an " + TTTGame.userTwoMark + " mark. \n")
            return # TODO check if this loop is having errors by there being no break statements 
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
            return askToPlayGame()               

# Ask whether the user wants to play again when a round has finished
def askToPlayAgain():
    
    answer = ''
    while (answer == ''):
        answer = input("Would you like to play another round? (y/n) \n")
        print('\n')
        if (answer == 'yes' or answer == 'y'):
            return playGame() 
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
    return               

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
    

def presentGameSummary():

    return

# Entry point for application
def main():		
	
    intro()
    askToPlayGame()
    playGame()
    
    return 0		# Exit application

if __name__ == "__main__": main()
   