class TicTacToeGame():
    """Class that contains the game logic"""

    # Getters
    def GetCurrentTurn(self):
        return self.__CurrentTurn

    def GetBoard(self,board):
        print('  ' + board[7] + '  |  ' +  board[8] + '  |  ' + board[9] + '   ')
        print('-----------------')
        print('  ' + board[4] + '  |  ' +  board[5] + '  |  ' + board[6] + '   ')
        print('-----------------')
        print('  ' + board[1] + '  |  ' +  board[2] + '  |  ' + board[3] + '   ')
        print('\n')
        
    def GetUserOneMark(self):
        return self.__UserOneMark

    def GetUserTwoMark(self):
        return self.__UserTwoMark
        
    def IsGameWon(self):
        return self.__bGameIsWon
    
    def IsGameDraw(self):
        return self.__bGameIsDraw

    def place_marker(self, board, marker, position):
        board[position] = marker

    def Reset(self): # set game to initial state
        self.__bGameIsWon = False
        self.__bGameIsDraw = False
        self.__UserOneMark = 'x'
        self.__UserTwoMark = 'o'
        self.__CurrentTurn = 'x'

    
    def __init__(self): # TODO class constructor
        
        self.__bGameIsWon = ''
        self.__bGameIsDraw = ''

        self.__CurrentTurn = ''
        self.__UserOneMark = ''
        self.__UserTwoMark = ''
        #self.Reset
         
      


