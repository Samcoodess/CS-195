import random
win=0
scoreCollection=()
loss =0
creatures=('monster','fox',)
items=('shield','boots',)
score,coins,currentHealth=0,0,20
userItem=()
allChoices=creatures+items
for i in range(1,1000):  
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
                            
                                    
                            # else:
                            #         pass
                            
                            
                    else:
                            print(f"you got attacked by {youGot}")
                            
                    if True:        
                            
                                    print(f'You killed the {youGot}')
                                    if youGot=="monster":
                                            score+=10
                                            print(f"Your score is now {score}") 
                                            
                                            
                                            
                                            print("Let's keep walking then")
                                            
                                            continue
                                    else:
                                            score+=1
                                            print(f"Your score is now {score}")
                                            
                                            
                                            print("Let's keep walking then")
                                            
                                            continue



                            
            elif youGot in items:
                    if youGot in userItem:
                            print(f"You already have {youGot}.Let's not make bag heavy ╰(◕ヮ◕)つ  \n")
                            
                            
                            
                            continue
                    else:
                            print(f"You got {youGot}\n It will be helpful to fight with creatures\n ฅʕ•̫͡•ʔฅ ")
                            
                            updatedUserItem=(youGot,)
                            userItem+=updatedUserItem
                            print(f'This is your item list {userItem}')
                            
                            
                        
            
            if score>=100:
                    scoreCollection +=(score,)
                    print("You won the game. \n 🏆ヽ(≧▿≦)ノ ")
                    print("Here is your trophy.")
                    
                    win=win+1
                                            
            if currentHealth<=0:
                    scoreCollection +=(score,)
                
                    print("Better luck from next time")
                    loss=loss+1
            
# winRate=(win-loss)/(win)*0.01
scoreSum= sum(scoreCollection)
averageScores=scoreSum/2
# print(f"The winrate is {winRate}%")
print(f"The average score is {averageScores}")
            

                                



        
        
              
              

