# =================================================================
# CMPUT 175 - Introduction to the Foundations of Computation II
# Lab 2 - Debugging: Tic-Tac-Toe
#
# ~ Created by CMPUT 175 Team ~
# =================================================================

SIZE = 3

class TicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = SIZE   # number of columns and rows of board
        
        # populate the empty squares in board with " "
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(" ")
            self.board.append(row)
   
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        # e.g. an empty board should look like this:
        #    0   1   2  
        # 0    |   |   
        #   -----------
        # 1    |   |   
        #   -----------
        # 2    |   |           
        
        print('   0   1   2 ')
        seperator = '  -----------'
        for x in range(len(self.board)):
            temp = []
            for y in self.board[x]:
                if y == " ":
                    temp.append("   ")
                elif y == "O": 
                    temp.append(' \033[91mO\033[0m ')
                elif y == "X":
                    temp.append(' \033[94mX\033[0m ')
                else:
                    temp.append(str(y))
            print(f'{x} {"|".join(temp)}')
            if x != len(self.board): 
                print(seperator)


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a symbol.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        #BUG HERE : Logic error
        
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.board[row][col] == " "
        return False
      
    
    
    def update(self, row, col, letter):
        '''
        Assigns the letter, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           letter (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        
        #BUG HERE:  Out of bound bug
        if 0<=row < self.size and 0<=col<self.size:
            if self.squareIsEmpty(row,col) == True: 
                self.board[row][col] = letter       
                return True
        return False
        
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        #BUG HERE: Logic error
         
        return all(cell != " " for row in self.board for cell in row)


    def isWinner(self, playerId):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        has their symbol (X or O). That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        sym= "O" if playerId==0 else "X" #BUG HERE 
        # Check rows
        for row in self.board:
             # BUG HERE: Logic Error
            if all(cell==sym for cell in row):
                return True
        #Check columns
        for col in range(self.size):
            # BUG HERE : Logic error
            if all(self.board[row][col]== sym for row in range(self.size)):
                return True
        # Check diagonals
        #BUG HERE : CALCULATION ERROR
        if all(self.board[i][i]== sym for i in range(self.size)):
            return True
        if all(self.board[i][self.size-i-1]== sym for i in range(self.size)):
            return True
            
        
        return False        
    


def main():
    #     TEST EACH METHOD THOROUGHLY HERE
    # suggested tests are provided as comments, but more tests may be required

    # start by creating empty board and checking the contents of the board attribute
    myBoard = TicTacToe()
    print('Contents of board attribute when object first created:')
    print(myBoard.board)

    # does the empty board display properly?
    myBoard.drawBoard()
    print("\n")
    #YES, THE EMPTY BOARD DISPLAYS PROPERLY

    # assign a number to an empty square and display
    update = myBoard.update(1,2,'X')
    myBoard.drawBoard()
    print("\n",update, "\n")
    # IT ASSIGNS NUMBER TO EMPTY CELL AND RETURNS TRUE

    # try to assign a number to a non-empty square. What happens?
    TryEmptyCell = myBoard.update(1,2,'O')
    myBoard.drawBoard()
    print("\n",TryEmptyCell,"\n")
    # IT DOES NOT ASSIGN THE NUMBER TO NON-EMPTY CELL AND RETURNS 'FALSE'

    myBoard.drawBoard()
    # THE BOARD DOESNT HAVE A WINNER AND NO, THERE CANNOT BE A WINNER AFTER 1 STEP, OT RETURNS 'FALSE'
    # check if the board has a winner. Should there be a winner after only 1 entry?
    print(f' {myBoard.isWinner(1)}',"\n")

    # check if the board is full. Should it be full after only 1 entry?
    print("\n",myBoard.boardFull(),"\n")
    # THE BOARD IS NOT FULL AND NO, IT CANNOT BE FULL AFTER 1 STEP

    myBoard.update(0,0,'O')
    myBoard.update(1,1,'O')
    myBoard.update(2,2,'O')
    myBoard.drawBoard()

    # check if the board has a winner
    print("\n",myBoard.isWinner(1), "\n")
    myBoard.drawBoard()
    print("\n")
    # YES, THE BOARD NOW HAS A WINNER AND IT RETUENS TRUE

    # check if the board is full

    # ADDED VALUES TO FILL THE BOARD
    myBoard.update(1,0,'X')
    myBoard.update(2,0,'O')
    myBoard.update(2,1,'X')
    myBoard.update(0,1,'O')
    myBoard.update(0,2,'X')
    myBoard.drawBoard()
    print("\n",myBoard.isWinner(0), "Player 1\n")
    print("\n",myBoard.isWinner(1), "Player 2\n")
    print("\n",myBoard.boardFull(),"\n")


if __name__ == "__main__":
    main()