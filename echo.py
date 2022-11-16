#Sambridhi Deo, CS 195 002

from ast import While

#greet user
print("Hello")

#take input from user
userResponse= input("Enter anything>> ")

#compare user's input and run the file until the user inputs q
while userResponse.lower() != "q":
    print(f"Well {userResponse.lower()} right back at ya")
    userResponse= input("Enter again>>> ")

print("Goodbye")
    