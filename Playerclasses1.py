#These are the player character classes

from random import randrange



class wizard:
    #creates the player character
        def __init__(self):
            self.hpp = 30
            self.aep = 50
            self.mapp = 2.5
            self.rapp = 2.5
            self.lp = 2
     #allows access and modification to the character's stats      
        def getHP(self):
            return self.hpp
        def setHP(self, x):
            self.hpp = self.hpp + x
            return self.hpp
        def getAE(self):
            return self.aep
        def setAE(self, x):
            self.aep = self.aep + x
            return self.aep
        def getMelee(self):
            return self.mapp
        def getRange(self):
            return self.rapp
        def getLuck(self):
            return self.lp
        def attacked(self):
        #If the player is attacked, the player's hit points decrease
                self.hpp = self.hpp - randrange(1,2)
                return print(self.hpp)
        def edied(self):
        #If the player's hit points = 0, the player is dead
                if self.hpp <= 0:
                    return True

       
class fighter:
    #creates player's character
        def __init__(self):
            self.hpp = 50
            self.aep = 30
            self.mapp = 4.0
            self.rapp = 1.0
            self.lp = 2
     #allows access to and setting of character's stats     
        def getHP(self):
            return self.hpp
        def setHP(self, x):
            self.hpp = self.hpp + x
            return self.hpp
        def getAE(self):
            return self.aep
        def setAE(self, x):
            self.aep = self.aep + x
            return self.aep
        def getMelee(self):
            return self.mapp
        def getRange(self):
            return self.rapp

        def getLuck(self):
            return self.lp
        def attacked(self):
        #If the player is attacked, the player's hit points decrease
                self.hpp = self.hpp - randrange(1,3)
                return print(self.hpp)
        def edied(self):
        #If the player's hit points = 0, the player is dead
                if self.hpp <= 0:
                    return True

        
class archer:
    #creates the player's character
        def __init__(self):
            self.hpp = 40
            self.aep = 40
            self.mapp = 2.5
            self.rapp = 3.5
            self.lp = 3

    #allows access to and setting of character's stats
        def getHP(self):
            return self.hpp
        def setHP(self, x):
            self.hpp = self.hpp + x
            return self.hpp
        def getAE(self):
            return self.aep
        def setAE(self, x):
            self.aep = self.aep + x
            return self.aep
        def getMelee(self):
            return self.mapp
        def getRange(self):
            return self.rapp
        def getLuck(self):
            return self.lp
        def attacked(self):
        #If the player is attacked, the player's hit points decrease
                self.hpp = self.hpp - randrange(1,2)
                return print(self.hpp)
        def edied(self):
        #If the player's hit points = 0, the player is dead
                if self.hpp <= 0:
                    return True
