import random
from tttlib import getValidMoves
 
def randomBotMove(mySpaces: set, opponentSpaces: set) ->set:
    '''get a random tic-tac-toe movement'''
    validMoves = list(getValidMoves(mySpaces | opponentSpaces) )
    return random.choice(validMoves)
 
def oneMoveBot(mySpaces:set,opponentSpaces:set) -> str:
    
    
    validMoves = list(getValidMoves(mySpaces | opponentSpaces) )
    return random.choice(validMoves)