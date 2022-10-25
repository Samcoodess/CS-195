
import random

 
score=0
coins=0
currentHealth =20
userItem = (1,)
while score<=100 or currentHealth>=0:
        print("\033[4\033[2J",end="")
        pass

        while True:
                print(f'score={score}  current health= {currentHealth}    coins={coins}\n\n')

                  
                print("****** :) You are walking :) ****** ")
                print("ᕕ( ᐛ )ᕗ.......ᕕ( ᐛ )ᕗ..\n")
                print(" Oh...Looks like you encountered with something,it can even be monster :=~~~~")
                print("let's see..what it is")
                print("(づ ͠°_ °)づ\n")
                creatures=('monster','fox')
                items=('shield','boots')
                allChoices=creatures+items
                youGot=random.choice(allChoices)
                for youGot in creatures:
                        if youGot=='monster':
                                print("Ooopss |⚆﹏⚆ |  \n :=~~~~~~ this monster with long tongue just attacked you ")
                                attackAmount= 7- len(userItem)
                                currentHealth-=attackAmount
                                print(f'your current Health is now {currentHealth}')
                                if currentHealth<=0:
                                        break
                                else:
                                        pass
                               
                                
                        else:
                                print(f"you got attacked by {youGot}")
                                attackAmount=7-len(userItem)
                                currentHealth-=attackAmount
                                print(f'your current Health is now {currentHealth}')
                                if currentHealth<=0:
                                        break
                                else:
                                        pass
                        print(f"Do you wanna fight with this {youGot}? \n (ง︡'-'︠)ง")
                        response=input("enter y for yes, and n for no \n")
                        if response =='y':
                                print(f'You killed the {youGot}')
                                if youGot=="monster":
                                        score+=10
                                        print(f"Your score is now {score}") 
                                        ans=input("press enter to keep walking")
                                        print(ans)
                                        
                                        print("Let's keep walking then")
                                        print("ᕕ( ᐛ )ᕗ.......ᕕ( ᐛ )ᕗ..\n")
                                        continue
                                else:
                                        score+=1
                                        print(f"Your score is now {score}")
                                        ans=input("press enter to keep walking")
                                        print(ans)
                                        print("Let's keep walking then")
                                        print("ᕕ( ᐛ )ᕗ.......ᕕ( ᐛ )ᕗ..\n")
                                        continue
                        if score>=100:
                                print("You won the game. \n 🏆ヽ(≧▿≦)ノ ")
                                print("Here is your trophy.")
                                break                        


        
                                
                for youGot in items:
                        for youGot in userItem:
                                print(f"You already have {youGot}.Let's not make bag heavy ╰(◕ヮ◕)つ  \n")
                                ans=input="press enter to keep walking"
                                print(ans)
                                print("ᕕ( ᐛ )ᕗ.......ᕕ( ᐛ )ᕗ..\n")
                                continue
                        else:
                                print(f"You got {youGot}\n It will be helpful to fight with creatures\n ฅʕ•̫͡•ʔฅ ")
                                print("Do you want to take shield?")
                                response=input("Enter y for yes and n for no >>")
                                if response== "y":
                                        userItem+=(youGot,)
                                        continue
                                else:
                                        ans=input("press enter to keep walking")
                                        print(ans)
                                        print("Let's keep walking then")
                                        print("ᕕ( ᐛ )ᕗ........ᕕ( ᐛ )ᕗ..\n")
                                        continue
        

                                



        
        
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              














































































































































































































































































































































































# # from calendar import c
# import random
# userItems=()
# uresponse=""
# coins=0
# score= 0
# currentHealth=20

# while True:
#         print(f'{score=} {currentHealth=} {coins=}')
#         print("\033[H\033[2J", end="")
#         userItems=()
#         uresponse=""
#         coins=int()
#         score= 0
#         read_key=int()
        
#         print("Do you wanna start the game?")
#         response=input("enter y for yes and n for no>>\n")
#         if response.lower()=="y":
#                 currentHealth=20
#         print(f"Let's go!!\n You have {currentHealth} healthpower for this level ")
#         test=('shield','monster','fox','ashok')
#         # items=('shield','boots','helmet','chest plate','gantlets')
#         # print(f'you may get one of these {items}')
#         # creatures=('monster,''rabbit','fox','rat')
#         creatures=('monster','fox')

#         # otherItems=('bush','big tree','rock')
#         otherItems=('bush','rock')
        
#         #     print(f"This is {A}")
#         while score<=100:
#                 A=random.choices(test)
        
#                 print(f"your score is {score}")
#                 print(f"Your currenthealth is {currentHealth}")
#                 print(f"Your coins is  {coins}")
        
#                 for A in userItems:
#                         print(f"You already have {A}.Let's not carry much weight and keep moving")
#                         print(f"This is your item list {userItems}")
#                         print("Enter to keep walking")
#                         input1=input("Press Enter to keep walking>>>")
#                         if input1=="a":  
#                                 continue
                        
#                 for A in not userItems:
#                         print(f"You got {A}")
                
#                         print('You can use shield to prtoect yourself.Do you want it?')
#                         uresponse=input("enter y for yes and n for no>>>\n")
#                         if uresponse.lower()=="y":
#                                 userItems= (f"{A},")
#                                 print(userItems)
#                                 continue
                        


#                 # elif A =='monster
                
#                 if A=="monster":
#                         print('OH....You got attacked by a monster')
#                         attackAmount= 7- len(userItems)
#                         currentHealth-=attackAmount
#                         print(f"Your current health is now {currentHealth}")
#                         print('Do you want to fight back?')
#                         answer = input("Enter y for yes and n for no >>>\n")
#                         if answer.lower()=='y':
#                                 print("WOAH....you killed the monster")
#                                 print(f"Your score is now {score+10}")
#                                 print(f"Your health is now {currentHealth}")
#                                 input1=input("Press Enter to keep walking>>>")
#                                 if input1=="":  
#                                         continue
                                
                        

                
#                 #     if A=='shield':
#         #     print("You can use it to protect yourself. Do you want a shield?")
#         #     uresponse=input("enter y for yes and n for no>>\n")
            
#         #     elif uresponse.lower()=="y":
#         #         userItems+=('shield',)
                
#         #     if A=='helmet':
#         #         print("You can use it to protect your head. Do you want a shield?")
#         #         uresponse=input("enter y for yes and n for no>>\n")
#         #     if uresponse.lower()=="y":
#         #         userItems+=('helmet',)
                
#         #     if A=='boots':
#         #         print("You can use it to walk in bush and rock. Do you want a shield?")
#         #         uresponse=input("enter y for yes and n for no>>\n")
#         #     if uresponse.lower()=="y":
#         #         userItems+=('boots',)
            
#         #     if A=='chest-plate':
#         #         print("You can use it to protect yourself while you fight with creatures. Do you want a shield?")
#         #         uresponse=input("enter y for yes and n for no>>\n")
#         #     if uresponse.lower()=="y":
#         #         userItems+=('chest-plate',)
                
#         #     if A=='gauntlets':
#         #         print("You can use it to protect yourself while creature fights. Do you want a shield?")
#         #         uresponse=input("enter y for yes and n for no>>\n")
#         #     if uresponse.lower()=="y":
#         #         userItems+=('gauntlets',)
                
#         #     if A=='bush' or'rock':
#         #         print("Oh you walked into bush")
#         #         for boots in userItems:
#         #             print("Don't wory you got your BOOOOOOTSSSSS!!:lifesaver")
#         #             continue
#         #         else:
#         #             print("You don't have boots. Your foot got injured")
                
#         #             print(f"your health is now {currentHealth-5}")
                    
#         # if A=='monster' or'fox':
#         #         print("shit..there was a moster.He attacked you.")
#         #         for shield in userItems:
#         #             print("Don't wory you got your SHIEEEEELD!!:lifesaver")
#         #             continue
#         #         else:
#         #             print("You don't have Shield. Your  got attacked")
#         #             print(f"your health is now {currentHealth-5}")

                
            
#         # #     for item in items:
#         # #         print(items)
#         # #     coins=""
#         # #     print(coins)
            
#         # # elif response.loer( )== "n":
#         # #     print("It is a fun game. i am sad you didn't try it."