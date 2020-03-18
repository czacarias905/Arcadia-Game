#Cecilia Zacarias
#3/2/2020

#This is scene 4 where the player has guess the correct trend but it is time to free her kingdom.
import scene3
import scene5
def begin():
    inventory = ["goldenkey", "Book", "model of kingdom", "box and silver key"]
    print("You have the guess the correct trend with these items now take the box and the silver key and head inside door 3")

    #Need to think of a way where if player does a mistake they will start from scene 2.

    print(input("Nyx takes the box and silver key and heads to door 3 Type opendoor3"))
    #look back 
    opendoor3 = print("Nyx has enter door 3 she needs the following: ")
    #inventory remove add variable
    print("box and silver key")

    print("In the middle of the room there is a table in the middle of the room place the box and silver key on table")

    table = []

    itemToAdd = input("Enter the item to add on table: ")

    table.append(itemToAdd)

    print("The following is on the table",(table))
    #feedback in loop make specific
    #opening the box with the silver key 
    #varible to equal print statement
    print("Lets use the silver key and open the box")
    box = []

    itemToAdd = input("Enter key, to open the box")

    key = print("you have inserted the: key")

    box.append(itemToAdd)


    #uncovering the the phrase the weill free Nyx's kingdom
    print(input("You have uncovered a pharse Type, \"The blue Sky isendless\", to free the kingdom"))
    i = input("You have uncovered a pharse Type, \"The blue Sky isendless\", to free the kingdom")

    if i == "The blue Sky isendless":
        print("continue")
        scene5.begin()

    else:
        print("So close to freeing the kingdom but not close enough")
        scene3.begin()
        con =input("Do you wish to go on?")           
        if con == "yes":
            print("Okay lets continue")
            scene5.begin()
        if con == "no":
            exit()
    # import statement very nessary
    # This is where the code begins
    #begin()
