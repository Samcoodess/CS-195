#Sambridhi Deo
#CS 195 002

from ast import While
from random import randint



#Generate a random number, store it as myNum 
myNum= randint(1,100)
userResponse=""
guess=10
response=""

#Take input from user and give user 10 chances to correctly guess a number
while guess!=0:
    userResponse=int(input("Guess a number between 1 to 100>>>\n"))
    
    #If user's guess is not a positive integer, tell user to enter a positive integer
    while userResponse<=0:
        print("Please enter a number greater than 0  :No symbols,no strings")
        userResponse=int(input("Enter a number>>>\n"))
        continue
       
    #Keep count of guesses    
    guess-=1
    
    #If user guesses correclty, say how many guess was left and ask if he wants to play again
    if userResponse==myNum:
        print("You guessed correctly")
        print(f"You still had  {guess} guesses left")
        print("Do you want to play again?")
        response= input("Enter Y for yes and N for No\n").lower()
        if response=="y": 
            print("How many guesses do you want?")
            guess= int(input(">>>"))
            myNum=randint(1,100)
            continue
        elif response== "n":
            break
        
    #If user guesses the number higher, tell him to guess a lower number than that    
    elif userResponse >=myNum:
        print("Your guess is little high, guess lower number")
        print(f"You have {guess} guesses left...")
        
     #If user guesses the lower number, tell him to guess a higher number   
    elif userResponse <=myNum:
        print("Your guess is little low, guess higher number")
        print(f"You have {guess} guesses left...")
     
     #If user runs out of a guess, tell them, and ask if u want to play again
      
    if guess==0:
        print(f"Sorry you used all your guesses. Your number was {myNum}") 
        print("Do you want to play a new game?")
        response= input("Enter Y for yes and N for No\n").lower()
        
         # IF yes, generate a new random integer and give him 10 guesses again
        if response=="y": 
            print("How many guesses do you want?")
            guess= int(input(">>>"))
            myNum=randint(1,100)
            continue
           
        #If no, say goodbye
        if response=="n":
            print("It was nice playing with you")  
    
    
    
            

    
    
   
        
        

 
        

