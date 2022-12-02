#CS195-Assignment 2- Sambridhi Deo
#Updated Program to calculate how many of you's is required to reach the moon using F-strings

#Declare the distance of moon as constant
DISTANCE_To_The_MOON= 40500000

#Ask user their name
name=input(" What\'s your name?>>")
#Give user personalized greeting by capitallizing and removing any spaces in their name
print( f"Hi, {name.strip().capitalize()} I am bot:your personal friend i.e Botfriend")

#Ask user their height 
height= int(input(f"How tall are you  in metre ? {name.strip().capitalize()} >>"))

#Calculate how many you's are required to reach the moon and print it
numberOfYouToReachMoon = int(DISTANCE_To_The_MOON/height)
print(f"Oh, we will require  {numberOfYouToReachMoon}  of you to reach the moon.")

#Ask user their weight             
print("Let\'s do it with weight now")
weighInEarth=int(input("Enter your weight in pounds"+">>>"))

#Calculate how much they weigh in moon in two decimal values and print it
weightInMoon= weighInEarth/6
print(f"Wow, You will only weigh {weightInMoon:.2f} pounds in moon.")
print(f"It was fun {name.strip().capitalize()} Bye\nHave a nice Day")
