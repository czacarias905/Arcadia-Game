#Cecilia Zacarias
#3/1/2020

# This is scene 2 of the game Arcadia
#Might need to debug to get it to work 
import scene3
def begin():
    inventory = ["golden key"]

    print("Nyx has arranged the doors in 3,4,5,2,1 it is time to open the doors where Nyx can find the items she needs to save her kingdom")

    #Player helps choose 3 doors given only 6 tries can not be 4 or 5 or it will restart going to debug
    d = ("  1,2,3".strip())
    x = 6

    while (x >= 6):
        numbers = input("Help Nyx to choose three door numbers you have 6 tries: ")
        x -= 1
        print("Too, bad. You tried one too many times.")
        #begin()
          
        if numbers == d:
            print("Nice work you got the doors that Nyx need lets open the first door retreive the golden key from inventory")
            break 
        else:
          print("One or two of the doors you selcted are not correct")
          begin()
 
    #create loop for the inventory and function to remove item for one time use 
    print(inventory) 

    input(" Lets open door 1 first, Type 'door1'")
    #finding items in the doors we unlock and adding to our inventory
    #create a function for specific can do a yes or no
    book = print("we have found a book in this door lets add to our inventory for later on")
    door1 = book

    #book = print("we have found a book in this door lets add to our inventory for later on")

    itemToAdd = input("Enter the item to add: ")

    inventory.append(itemToAdd)

    input(" Lets open door 2, Type door2")
    model_kingdom = print("we have found a model of the kingdom lets add to out inventory for later on")

    door2 = model_kingdom

    #model_kingdom = print("we have found a model of the kingdom lets add to out inventory for later on")

    itemToAdd = input("Enter the item to add: ")

    inventory.append(itemToAdd)

    input(" Lets open door 3 first, Type door3")
                        
    box_silverkey = print("we have found a box and silver key in this doors lets add to our inventory for later on")

    door3 = box_silverkey
                        
    #box_silverkey = ("we have found a box & silver key in this doors lets add to our inventory for later on")

    itemToAdd = input("Enter the item to add: ")

    inventory.append(itemToAdd)

    print("lets check our inventory to see if everything was added type inventory")
    print(inventory)

    GoOn =input("Do you wish to go on?")           
    if GoOn == "yes":
        print("Okay lets continue")
        scene3.begin()

    elif GoOn == "no":
        exit()
    

#this is where the code starts
#begin()


