#Cecilia Zacarias
#3/1/2020

#this the intro for the game Arcadia these are the functions that will be used in the intro.

# This is what the player will see when running the game 
import scene2      
#import scene2
print("Nyx has said goodbye to her family and makes her way to the enchanted castle. It is the last time she gazes at the parchment dome above her that has her entire kingdom enclosed. She enters the castle and not finding anyone in sight Nyx sits down leaning against the wall and accidently falls asleep")

input("Wake up Nyx to begin her journey type AWAKE")

AWAKE = print("There is a golden key next to Nyx add to inventory this could be used later on")

#adding a item to inventory

inventory = []

itemToAdd = input("Enter the item to add: ")

inventory.append(itemToAdd)

print(inventory)

#Commanding character to take an action 
print(input("Nyx takes the key and sees stairs going upwards type climb"))

climb = print("Nyx has reached the top and sees five doors. Help Nyx figure out which door correlates with the following numbers 1,2,3,4,5. Be careful because there are two doors that are empty")
#This block is where the players asked to arrange a set of numbers 
x = 5
Doors = "3,4,5,2,1"
while (x>0):
    arrange = input("How would you arrange the numbers?: ")

    #arrange2 = input("Try again in arranging the numbers")
    x-=1

    if arrange == Doors:
        print("This is correct you may continue!")
        scene2.begin()
    else:
        print("Try again")

##    elif arrange2 == Doors:
##        print("This is correct you may continue!")AWAKE
##        scene2.begin
##    else:
##        print("This is not correct",arrange2)
##
##    while x <= 5:
##        x = x - 1
##    print("You tried one too many times", restart)       

restart =input("Do you wish to start again?")           
if restart == "yes":
    begin()

elif restart == "no":
    exit()
#this is where the code starts
begin()

