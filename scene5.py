#Cecilia Zacarias
#3/2/2020

#This is scene 5 of the game arcadia this is the end of Nyxs journey
def begin():
    print("The room has vanished, and Nyx lays on the grass asleep and awakens by the bright sun")

    #player is given a choice for the characters next action
    print(input("Nyx looks at the sky and is surprise to see a blue sky, she notices a girl pass by should next as what happen to the dome or should she let it be? Type Ask to talk to girl or Type Pass to let it be"))
    #make sure it moves from print 
    #Ending of the game could go either two ways 
    Ask = print("Passerby gives her a glare and says that there was never a parchment dome")

    Pass = print("Nyx gets up and begins to walk")
    #rethink might not work 
    i = [Ask, Pass]

    if i is Ask:
        print("Nyx looks at the sky again and shakes her head everything she went through never happened")

    elif i is Pass:
        print("Nyx decides to live in confusion not knowing what exaclty happen to her and her village and heads home, End of Game")

    print("End of Game")
    exit()
    #this is where the code begins
    #begin()
