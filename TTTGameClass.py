class TicTacToeGame():
    """Class that contains the game logic"""

    board = [''] * 10

    # Getters
    def GetCurrentTurn(self):
        return __MyCurrentBoard

    def place_marker(board, marker, position):
        board[position] = marker

    def GetBoard(self):
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('-----------')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('-----------')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        
    def GetUserOneMark(self):
        return

    def GetUserTwoMark(self):
        return
        
    def IsGameWon(self):
        return 
    
    def IsGameDraw(self):
        return

    def Reset(self): # set game to initial state
        self.__bGameIsWon = False
        self.__bGameIsDraw = False
        self.__UserOneMark = 'x'
        self.__UserTwoMark = 'o'
        #self.__MyCurrentBoard = board
        self.__MyCurrentTurn = 'x'

    
    def __init__(self): # TODO class constructor
        board = []
        self.__bGameIsWon = ''
        self.__bGameIsDraw = ''

        self.__MyCurrentTurn = ''
        self.__MyCurrentBoard = '' 
        self.__UserOneMark = ''
        self.__UserTwoMark = ''
        self.Reset
         
      


