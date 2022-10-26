import random

creatures=('monster','fox',)
items=('shield','boots',)
score,coins,currentHealth=0,0,20
userItem=()
allChoices=creatures+items

while score<=100 or currentHealth>=0:
        print("\033[4\033[2J",end="")
        print(f'score={score}  current health= {currentHealth}    coins={coins}\n\n')
        # pass

            
        print("****** :) You are walking :) ****** ")
        print(" Oh...Looks like you encountered with something,it can even be monster :=~~~~")
        print("let's see..what it is")
        youGot=random.choice(allChoices)
        if youGot in creatures:
                if youGot=='monster':
                        print("Ooopss   \n :=~~~~~~ this monster with long tongue just attacked you ")
                        attackAmount= 7- len(userItem)
                        currentHealth-=attackAmount
                        print(f'your current Health is now {currentHealth}')
                       
                        #         pass
                        
                        
                else:
                        print(f"you got attacked by {youGot}")
                        
                if True:        
                        print(f"Do you wanna fight with this {youGot}? \n (ง︡'-'︠)ง")
                        playerResponse=input("enter y for yes, and n for no ")
                
                        if str(playerResponse) =='y':
                                print(f'You killed the {youGot}')
                                if youGot=="monster":
                                        score+=10
                                        print(f"Your score is now {score}") 
                                        
                                        ans=input("press enter to keep walking")
                                        print(ans)
                                        # print("\033[4\033[2J",end="")
                                        print("Let's keep walking then")
                                        
                                        continue
                                else:
                                        score+=1
                                        print(f"Your score is now {score}")
                                        ans=input("press enter to keep walking")
                                        print(ans)
                                        # print("\033[4\033[2J",end="")
                                        print("Let's keep walking then")
                                        
                                        continue



                        
        elif youGot in items:
                if youGot in userItem:
                        print(f"You already have {youGot}.Let's not make bag heavy ╰(◕ヮ◕)つ  \n")
                        ans=input="press enter to keep walking"
                        print(ans)
                        # print("\033[4\033[2J",end="")
                        
                        continue
                else:
                        print(f"You got {youGot}\n It will be helpful to fight with creatures\n ฅʕ•̫͡•ʔฅ ")
                        print(f"Do you want to take {youGot}?")
                        response_2=input("enter y for yes, and n for no \n")
                        if str(response_2) =='y':
                                updatedUserItem=(youGot,)
                                userItem+=updatedUserItem
                                print(f'This is your item list {userItem}')
                        
                                continue
                        else:
                                ans=input("press enter to keep walking")
                                print(ans)
                                # print("\033[4\033[2J",end="")
                                print("Let's keep walking then")
                                
                                continue
        
if score>=100:
        print("You won the game. \n 🏆ヽ(≧▿≦)ノ ")
        print("Here is your trophy.")
                                
elif currentHealth<=0:
        print("Better luck from next time")
                                



        
        
              
              

