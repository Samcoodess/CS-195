import sys
from tttlib import humanMove, playGame
from tttai import randomBotMove, oneMoveBot
 
INSTRUCTION = '''
    Please run ttt.py player player
    Where player can be
    h - human player
    r - randomBot
    '''
 
PLAYERS = {
        'h' : humanMove,
        'r' : randomBotMove,
        'o' : oneMoveBot
    }
def help():
    print(INSTRUCTION)
 
if __name__ == '__main__':
    if len(sys.argv) == 3 \
        and sys.argv[1] in PLAYERS \
        and sys.argv[2] in PLAYERS:
 
        playGame(PLAYERS[sys.argv[1]], PLAYERS[sys.argv[2]],)
 
    else:
        help()
