import random

board_list=list(range(1,10))
board= ("""
{} | {} | {}
---+---+---
{} | {} | {}
---+---+---
{} | {} | {}
""").format(*board_list)
print(board)  
print(board_list)  
       
# def tic_tac_toe(resp1:int):
def player1(resp1:int):
    # assert resp1 in range(1,10),"Your response must be between 1 and 9"
    if int(resp1) in range(1,10):
        board_list[int(resp1)]="0"
        print(board_list)
        
        print(resp1)
    return resp1

player1(resp1=input("Where do you want to place your O?>>"))

def player2(resp2:int):
    # assert resp1 in range(1,10),"Your response must be between 1 and 9"
    if int(resp2) in range(1,10):
        board_list[int(resp2)]="0"
        print(board_list)
        
        print(resp2)
    return resp2

player2(resp2=input("Where do you want to place your O?>>"))
# tic_tac_toe()    
        
        
        

