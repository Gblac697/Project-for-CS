class chara_trait: #charaters stats
    def __init__ (self, name, health, arm):
        self.name = name
        self.health = health
        self.arm = arm
        self.inventory = []
    def is_alive(self):
        return self.health > 0
      
    #actions for player to use
    def throw(self, rope, boat):
     print("you throw the rope on the boat")
     if rope in self.inventory and self.arm >3:
         print("You got the boat")
         self.inventory.append(boat)
     elif rope.speed < 3:
        print("You can not reach the boat")
     else:
         print("you failed to throw")
         
    def route(self, map):
        if map in self.inventory:
            print("You have found da Way!")
        else:
            print("You are lost")
            pass
    
    def sail(self,boat):
        if boat in self.inventory:
            print("You sail home. You WIN!")
        else:
            print("You cannot")
            pass
player_one_name = "You" 
player_one = chara_trait(player_one_name,100,10)
old_man_name= "Old Pete"
old_man = chara_trait(old_man_name,100,10)

#class for items
class items_used:
    def __init__(self, stregth, weight, speed, ):
        self.stregth = stregth
        self.weight = weight
        self.speed = speed 

map = items_used(1,1,10,)
rope = items_used(2,2,5)
boat = items_used(20,10,12)
axe = items_used(5,5,3)
boards = items_used(1,1,1)


    