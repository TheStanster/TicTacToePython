class TicTacToeGame():
    """Class that contains the game logic"""
    
    def Reset(self): # set game to initial state
        self.bGameIsWon = False
        self.bGameIsDraw = False
        
        self.currentTurn = 1
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


       
         
      


