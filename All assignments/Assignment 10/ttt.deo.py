import random

board_list=list(range(1,10))

def display_board(board_list:list,board:str):
    print(board)

display_board(board_list=list(range(1,10)),board= ("""
{} | {} | {}
---+---+---
{} | {} | {}
---+---+---
{} | {} | {}
""").format(*board_list))  

       
# def tic_tac_toe(resp1:int):
def player1(resp1:int):
    # assert resp1 in range(1,10),"Your response must be between 1 and 9"
    if int(resp1) in range(1,10):
        board_list[int(resp1)-1]="o"
        print(resp1)
        display_board(board_list,board=("""
{} | {} | {}
---+---+---
{} | {} | {}
---+---+---
{} | {} | {}
""").format(*board_list))
        
        
    return resp1

player1(resp1=input("Where do you want to place your O?>>"))

def player2(resp2:int):
    # assert resp1 in range(1,10),"Your response must be between 1 and 9"
    if int(resp2) in range(1,10):
        board_list[int(resp2)-1]="X"
        print(resp2)
        
        display_board(board_list,board=("""
{} | {} | {}
---+---+---
{} | {} | {}
---+---+---
{} | {} | {}
""").format(*board_list))
        
        
    return resp2

player2(resp2=input("Where do you want to place your X?>>"))


  
        
        
        

