#Cecilia Zacarias-he player needs to figure out what the items collected mean./5r
# retrives items from inventory
#inventory = ["goldenkey", "Book", "model of kingdom", "box and silver key"]
import scene4
inventory = ["goldenkey", "Book", "model of kingdom", "box and silver key"]

def begin():
    input("Nyx has found all three items she needs to save her kingdom, but what do these items mean lets pull up the items in the iventory Type inventory")
    print(inventory)
    #trend = input("What is the trend behind these three items? type i for hint: ")

#User must guess the phrase "enchanted" after the six try player will be given a hint 
    x = input("Hint one word 9 letters, two letters given the first is e the second is d")
    t = 6
    word = "enchanted"
    i = print("Hint one word 9 letters, two letters given the first is e the second is d")
    #while t <= 6:
       # t -= 1
        #x = input("What is the trend behind these three items? type i for hint: ")
        #i = print("Hint one word 9 letters, two letters given the first is e the second is d")
    
    if x == word:
        input("Nice you got the the trend, Type Next and read carefully the instructions")

    else:
        print("that is incorrect try again")
        print(x)
#add a loop
#Need to think of a way where if player does a mistake they will start from scene 2.
    Next = print(" It is time to take the next steps in Nyx's journey, be very carefull in the following task make a mistake and you will be where it began")
    con =input("Do you wish to go on?")           
    if con == "yes":
        print("Okay lets continue")
        scene4.begin()

    elif con == "no":
        exit()
#begin()
