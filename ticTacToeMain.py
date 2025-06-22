
import time, os
from ticTacToe import TicTacToe

def clear():
    '''
    clears the screen
    '''
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')


def getCoord(player, dimension):
    '''
    Prompts for an index value corresponding to either the row or column (as
    described by dimension) of a square on the board
    Inputs:
       player (int) - number of current player (1 or 2)
       dimension (str) - describes what the index relates to (e.g. 'row' or 'column')
    Returns: int index (either row or column)
    '''
    #BUG HERE: Out of bound bug
    LOWER = 0
    UPPER = 2
    index = input('Player ' + str(player) + ', please enter a ' + dimension+': ')
    while True:
        if index.isdigit() and int(index) in range(LOWER, UPPER+1):
            return int(index)
        else:
            index = input(f"Invalid input! Please enter a valid {dimension}: ")


def isGameOver(myBoard, player):
    '''
    The game is over if the current player has won, or there are no empty squares
    left for the next player to select.
    Inputs:
       myBoard (TicTacToe) - object containing current state of game board
       player (int) - number of current player (1 or 2)
    Returns: True if game if over; False otherwise
    '''
    if myBoard.isWinner(player):
        clear()
        myBoard.drawBoard() #BUG HERE : Functional bug
        print (f'Player', {player} ,"wins. Congrats!")           
        return True
    elif myBoard.boardFull():
        clear()
        myBoard.drawBoard()  #BUG HERE: Functional bug
        print ("It's a tie.")             
        return True
    return False


def playAgain():
    '''
    Asks if a new game should be started. A valid answer is any entry that begins
    with y/Y/n/N.
    Inputs: none
    Returns: True if a new game should start; False otherwise
    '''
    playAgain = '' #BUG HERE :Logic error
    # validate user's input
   
    while not playAgain or playAgain[0].upper() not in ['Y', 'N']:  # Ensure playAgain is non-empty
        playAgain = input("Do you want to play another game? (Y/N) ").strip()  # Remove spaces

    return playAgain[0].upper() == "Y"       


def main():
    '''
    Controls the game flow for a 2-player version of Numerical Tic Tac Toe.
    Inputs: none
    Returns: None
    '''
    newGame = True
    while newGame:
        TITLE = "Starting new Numerical Tic Tac Toe game"
        print("-"*len(TITLE))
        print (TITLE)
        print("-"*len(TITLE))
        myBoard = TicTacToe()
        gameOver=False
        turn = 0
        while not gameOver:
            myBoard.drawBoard()
            
            # get input from user
            entry = ['O','X'][turn]
            
            row = getCoord(turn+1, 'row')
            col = getCoord(turn+1, 'column')
                                   
            # update board and check if game continues
            if myBoard.update(row, col, entry):
                print(f"Player {turn+1}'s turn ended")
                gameOver = isGameOver(myBoard, turn+1)
                turn = 1-turn  #BUG HERE: Functional Bug          
            # need to reprompt for new input for given player   
            else:
                print('Error: could not make move!')
            time.sleep(1)
        clear()
        newGame = playAgain()    #BUG HERE: System level integration bug 
            
    print('Thanks for playing! Goodbye.')
            
    
main()
          
