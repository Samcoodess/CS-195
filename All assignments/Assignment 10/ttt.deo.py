import random

board_list=list(range(1,10))
player1_board=[]
player2_board=[]

def display_board(board_list:list,board:str):
    print(board)

display_board(board_list=list(range(1,10)),board= ("""
{} | {} | {}
---+---+---
{} | {} | {}
---+---+---
{} | {} | {}
""").format(*board_list))  

winner= [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
# while winner not in player1_board or winner not in player2_board:       
def player1(resp1:int):
    # assert resp1 not in range(1,10),"Your response must be between 1 and 9"
    # assert resp1.upper()== "X","This spot is already taken by X"
    # assert resp1.upper()== "0","You already chose this spot"

    if int(resp1) in range(1,10):
        board_list[int(resp1)-1]="O"

        print(resp1)
        display_board(board_list,board=("""
{} | {} | {}
---+---+---
{} | {} | {}
---+---+---
{} | {} | {}
""").format(*board_list))
        
        
    return resp1

player1(resp1=input("Where do you want to place your O?>>>>"))

def player2(resp2:int):
    # assert resp2 not in range(1,10),"Your response must be between 1 and 9"
    # assert resp2.upper()== "O","This spot is already taken by O"
    # assert resp2.upper()== "X","You already chose this spot"
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



    
    
    

