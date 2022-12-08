
from os import system, name

BOARD_SPACES = '1','2','3','4','5','6','7','8','9'
WINNERS = ('1','2','3'), ('4','5','6'),('7','8','9'), ('3','5','7'),('1','5','9'),('1','3','7'),('3','6','9')
 

# clears the screen

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')




def displayBoard(xSpaces:set,oSpaces:set):
    # set up the board, replace spaces wit x's and o's
    board = list (BOARD_SPACES) 
    for i, space in enumerate(board):
        if space in xSpaces:
            board[i] = 'X'
 
        elif space in oSpaces:
            board[i] = 'O'
    
    clear()
    
     #print board
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')


 
def isWinner(spaces:set) -> bool:
    '''Return true is if spaces contains any of the combinations in WINNERS'''
    for combo in WINNERS: 
        if spaces.issuperset(combo):
            return True


def getValidMoves(takenSpaces:set) -> set:
    '''Returns the set of BOARD_SPACES that are not in takenspaces'''
    return set(BOARD_SPACES) - takenSpaces

def playGame(playerXmove:callable,playerOmove:callable):
    #initial tic-tac-toe board
    xSpaces = set()
    oSpaces = set()
#game loop
    while True:
        #X moves
        move = playerXmove(xSpaces, oSpaces)
        xSpaces.add(move)
        if isWinner(xSpaces):
            displayBoard(xSpaces, oSpaces)
            print('X Wins!')
            return 'X'
 
        elif not getValidMoves(xSpaces|oSpaces):
            displayBoard(xSpaces,oSpaces)
            print('Draw.')
            return ''
 
        #O moves
        move = playerOmove(oSpaces,xSpaces)
        oSpaces.add(move)
 
        if isWinner(oSpaces):
            displayBoard(xSpaces,oSpaces)
            print('O Wins!')
            return 'O'
 
def humanMove(mySpaces:set,opponentSpaces:set) -> str:
    '''get Valid tic-tac-toemove from human player'''
    validSpaces = getValidMoves(mySpaces|opponentSpaces)
    if len(opponentSpaces) > len(mySpaces):
        displayBoard(opponentSpaces, mySpaces)
        print('You are playing as O\'s')
    else:
        displayBoard(mySpaces,opponentSpaces)
        print('Your are playing as X\'s')
 
    move = input('Please select a space: ')
    while move not in validSpaces:
        print('This is not a valid move')
        move = input('Please select a valid space: ')
 
    return move 

 
if __name__=='__main__':
     playGame(humanMove,humanMove)

    
    