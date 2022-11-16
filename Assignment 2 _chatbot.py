#CS195-Assignment 2- Sambridhi Deo
#Program to calculate how many of you's is required to reach the moon

#Declare the distance of moon as constant
DISTANCE_To_The_MOON= 40500000

#Ask user their name and greet them
name=input(" What\'s your name?>>")
print ("Hi " +name + " I am bot:your personal friend i.e Botfriend")

#Ask user their height  
height= input("How tall are you  in metre ? "+name+ " >>")

#Calculate how many you's are required to reach the moon and print it
numberOfYouToReachMoon = int(DISTANCE_To_The_MOON/float(height))
print("Oh, we will require " + str(numberOfYouToReachMoon)+ " of you to reach the moon.")

#Ask user their weight 
print("Let\'s do it with weight now")
weighInEarth=int(input("Enter your weight in pounds"+">>>"))

#Calculate how much they weigh in moon and print it
weightInMoon= int(weighInEarth/6)
print("Wow, You will only weigh "+ str(weightInMoon)+" pounds "+ " in moon")
print("It was fun "+ name+ " Bye ")
