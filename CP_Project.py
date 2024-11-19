from Stat_Sheet import * #Charater and items import

#start the game
def player_spawn(player_one):

    print("You are lost in forest.")
    print("you see three paths ahead")
    print("North is the Mountain, West to the Lake, East to the Valley.")

    choice = input("Onward. (North/West/East): ").lower()
    
    if choice == "north":
        mountain()
    elif choice == "west":
        lake()
    elif choice == "east":
        valley()
    else:
        print("You failed that")
        return player_spawn(player_one)
#Forest return Loc
def forest():
    print("You are back in the forest")
    if axe in player_one.inventory:
     pass
    else:
     print("You see an axe leanign on the tree.")
    choice = input("Onward. (North/West/East): ").lower()
    
    if choice == "north":
        mountain()
    elif choice == "grab axe":
        print ("You try to grab the axe")
        if axe in player_one.inventory:
            print("You have that")
            return forest()
        elif axe not in player_one.inventory: 
             print("you grab axe.")
             player_one.inventory.append(axe)
             return forest()
        else:
            pass
    elif choice == "west":
        lake()
    elif choice == "east":
        valley()
    else:
        print("You failed that")
        return forest()
#Mountain Loc
def mountain():
    print("You arrive at the Mountain")
    print("You see a House and some rock")
    print("Along with two road to the lake and valley")
    if rope in player_one.inventory: #rope spawn
     pass
    else:
     print("You see a rope hang tree")
    
    choice = input("Now what? (Head Back/Enter House/ Climb the Rocks/ Go to lake/ Go to valley): ").lower()

    if choice == "go to valley":
        print("To the Valley")
        valley()
    elif choice == "go to lake":
        print("To the Lake")
        lake()
    elif choice == "head back":
        print("You go back to Forest")
        forest()
    elif choice == "enter house":
        print("the door is locked.")
        
        if  boards in player_one.inventory:
            print("However, You enter the house through a nice hole.")
            house()
        elif axe in player_one.inventory:
         print("Do you want to cut down the locked door")
         choice = input("(Yes/ No):").lower()
         if choice == ("yes"):
             print("You cut down the door.")
             player_one.inventory.append(boards)
             house()
         else:
             print("You head back")
             return mountain()
        else:
         print("The door is locked")
         return mountain()
    elif choice=="climb the rocks":
        print("rock time")
        print('You climb to a cliff edge. You meet God and become wise.')
        print('Now you do not need to escape. Game Over!')
        stop()
    elif choice == "grab rope":
        print ("You try to grab the rope")
        if rope in player_one.inventory:
            print("You have that")
            return mountain()
        elif rope not in player_one.inventory: 
             print("you grab rope.")
             player_one.inventory.append(rope)
             return mountain()
        else:
            pass
    else:
        print("You know you are wrong")
        return mountain() #loop if input is inncorrect
#the house Loc  
def house():
    print("You enter the house.")
    print("You see an old man.")
    
    choice = input("Now what? (Talk to Man/ Head back/ Attack the man):").lower()
#inputs
    if choice == "head back":
        print("You go back")
        mountain()
    elif choice == "talk to old man":
        print("You approch old man")
    else:
        print("You know you are wrong")
        return house()    
#Lake Loc
def lake():
    print('You arrive at the Lake.')
    print("You see a road to the Mountain.")
    if boat in player_one.inventory:
        pass
    else:
     print("You see a boat floating.")
    
    choice = input("(Head Back/go to road):").lower()
    if choice == "throw rope":
        player_one.throw(rope,boat)
        pass
    else:
        pass


    if choice == "head back":
        print("You go back to Forest")
        forest()
    elif choice == "go to road":
        print("You walk up the road.")
        mountain()
    elif choice == "sail home":
        player_one.sail(boat)
        finish_line()
    else:
        print("You know you are wrong.")
        return lake()
    
   
 #Valley area   
#Valley Loc
def valley():
    print("You arrive to the Valley.")
    print("It is a sea of green grass")
    if map in  player_one.inventory:
        print("The map shows da way")
        pass
    else:
        pass

    choice = input("(head back/Take Road to mountain/Go to the Green Sea):").lower()
    if choice == "head back":
        print("You go back to Forest")
        forest()
    elif choice == "take road to mounatain":
        mountain()
    elif choice == "go da way":
        print("You found da way")
        finish_line()
    elif choice == "go to the green sea":
        print("You walk into the sea lost forever. GAME OVER")
    else:
        print("You know You are wrong")
        return valley()
def man_speak():
    
#Victory Message
def finish_line():
     print("You are the Master of Game.")
     stop()
#game loop
def stop():
    print("Do you want to play again?")
    choice = input("(Play again/Stop playing):").lower()
    if choice == "play Again":
        player_spawn(player_one)
    elif choice == "stop playing":
        print("Thanks for Playing")
    else:
        print("What?")
        stop()
#Start call  
if __name__ == "__main__":
    player_one = chara_trait(100,10)
    player_spawn(player_one)
   