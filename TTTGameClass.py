class TicTacToeGame():
    """Class that contains the game logic"""
    
    def Reset(self): # set game to initial state
        self.bGameIsWon = False
        self.bGameIsDraw = False
        
        self.currentTurn = 0
        self.currentMark = ''
        self.playerNum = ''
        
    
    def __init__(self): # class constructor
        
        self.bGameIsWon = ''
        self.bGameIsDraw = ''

        self.userOneMark = 'x'
        self.userTwoMark = 'o'
        self.currentTurn = ''
        self.currentMark = ''
        self.playerNum = ''
        
     
    def BoardCheck(self, board, mark):
        if self.currentTurn == 9:
            self.bGameIsDraw = True

        else: 
            self.bGameIsWon = self.IsGameWon(board, mark)


    def IsGameWon(self, board, mark):
        return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
        (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
        (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
        (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
        (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
        (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
        (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
        (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
              

       

        # Getters
    def NextTurn(self):
        self.currentTurn += 1

    def GetBoard(self,board):
        print('  ' + board[7] + '  |  ' +  board[8] + '  |  ' + board[9] + '   ')
        print('-----------------')
        print('  ' + board[4] + '  |  ' +  board[5] + '  |  ' + board[6] + '   ')
        print('-----------------')
        print('  ' + board[1] + '  |  ' +  board[2] + '  |  ' + board[3] + '   ')
        print('\n')
    
    def GetCurrentPlayerMark(self):
        if self.currentTurn % 2 == 1:
            self.currentMark = self.userOneMark
        else:
            self.currentMark = self.userTwoMark

    def GetCurrentPlayerNumber(self):
        if self.currentTurn % 2 == 1:
            self.playerNum = '1'
        else:
            self.playerNum = '2'


    def place_mark(self, board, mark, position):
        board[position] = mark


       
         
      


