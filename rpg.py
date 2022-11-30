#Sambridhi Deo
#CS_195

#importng the package random 
import random

#create tuples for items
creatures=('monster','fox','rabbit','rat',)
items=('shield','boots','chest-plate','gauntlets')
otherThings=('bush','big tree','rock',)

#Give value for sore,coins,current health
score,coins,currentHealth=0,0,20

#create a empty tuple for user where user will add items after picking up
userItem=()

#add all the tuples
allChoices=creatures+items+otherThings

#run the code as long as score is less than hundred or current health is greater than 0
while score<=100 or currentHealth>=0:
        
        #clear the screen
        print("\033[4\033[2J",end="")
        
        #update the scores, current Health ,coins, user Items after every loop
        print(f'score={score}  current health= {currentHealth}    coins={coins}    useritem={userItem}\n\n')
        
        #engage with user as the game starts    
        print("****** :) You are walking :) ****** ")
        print(" Oh...Looks like you encountered with something,it can even be monster :=~~~~")
        print("let's see..what it is")
        
        #select random from the tuple allchoices
        youGot=random.choice(allChoices)
        
        #if the object user got is in creatures tuple, run this 
        if youGot in creatures:
                
                #if the object user got is monster, run this
                if youGot=='monster':
                        print("Ooopss   \n :=~~~~~~ this monster with long tongue just attacked you ")
                        
                        #calculate attackamount by subtracting number ofitems in user list from 7
                        attackAmount= 7- len(userItem)
                        
                        #calculate the current health by subtracting attack amount
                        currentHealth-=attackAmount
                        print(f'your current Health is now {currentHealth}')
                       
                       
                        
                #if the object is in creatures but not monster, run this        
                else:
                        print(f"you got attacked by {youGot}")
                
                #ask user if he wants to fight back       
                # if Tru        
                print(f"Do you wanna fight with this {youGot}? \n (ง︡'-'︠)ง")
                resp=input("enter y for yes, and n for no ")

                #if user response isn't equal to n, run this
                if resp.lower() !='n':
                        print(f'You killed the {youGot}')
                        
                        #if user had gotten monster, run this
                        if youGot=="monster":
                                
                                #increase user's score by 10
                                score+=10
                                print(f"Your score is now {score}") 
                                
                                #press enter to keep walking
                                ans=input("press enter to keep walking>>")
                                print(ans)
                                print("Let's keep walking then")
                                # continue
                        
                        #if user had gotten any other creatures but not monster
                        else:
                                
                                #increase user's score by 1
                                score+=1
                                print(f"Your score is now {score}")
                                
                                #press enter to keep walking
                                ans=input("press enter to keep walking>>>")
                                print(ans)
                                print("Let's keep walking then")
                                
                                # continue



        #if user gets an object that isn't creature but is a object, run this                
        elif youGot in items:
                
                #check if user already has the item
                if youGot in userItem:
                        
                        #if user has the item, keep moving
                        print(f"You already have {youGot}.Let's not make bag heavy ╰(◕ヮ◕)つ  \n")
                        ans=input("press enter to keep walking>>>")
                        print(ans)
                       
                        
                        continue
                
                #if user doesn't have the item, ask user if he wants to pick it up
                else:
                        print(f"You got {youGot}\n It will be helpful to fight with creatures\n ฅʕ•̫͡•ʔฅ ")
                        print(f"Do you want to take {youGot}?")
                        
                        #if user doesn't say no, run this
                        respo_2=input("enter y for yes, and n for no \n")
                        if respo_2.upper() !='N':
                                
                                #add the item user picked in his item list 
                                updatedUserItem=(youGot,)
                                userItem+=updatedUserItem
                                print(f'This is your item list {userItem}')
                        
                                continue
                        
                        #if user had said n, keep moving
                        else:
                                ans=input("press enter to keep walking>>>")
                                print(ans)
                              
                                print("Let's keep walking then")
                                
                                continue
                        
        #if user got object, that isnt't in creatures, items, then run this
        elif youGot in otherThings:
                print(f"Oh..it's just a {youGot}")
                ans=input("press enter to keep walking>>>")
                print(ans)
                continue
                
#if loop was ended and score was more than 100, tell user they won              
if score>=100:
        print("You won the game. \n 🏆ヽ(≧▿≦)ノ ")
        print("Here is your trophy.")

#if loop was ended and current health was less than 0, tell user they lost game                                
elif currentHealth<=0:
        print("Better luck from next time")
                                



        
        
              
              

