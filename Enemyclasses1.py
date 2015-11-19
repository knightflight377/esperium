#These are the enemy classes (includes boss)

from random import randrange

class enemy:
    
    #creates enemy character
        def __init__(self):
            self.hpp = 35
            self.aep = 15
            self.mapp = 3.0
            self.rapp = 1.0
            self.lp = 1
     #allows access to and setting of enemy's stats     
        def getHP(self):
            return int(self.hpp)
        def setHP(self, x):
            self.hpp = self.hpp + x
            return self.hpp
        def getAE(self):
            return int(self.aep)
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
        #If the enemy is attacked, the enemy's hit points decrease
                self.hpp = self.hpp - randrange(1,8)
                return print(self.hpp)
        def edied(self):
        #If the enemy's hit points = 0, the enemy is dead
                if self.hpp <= 0:
                    return True


class boss:

        def __init__(self):
            self.hpp = 120
            self.aep = 20
            self.mapp = 5.0
            self.rapp = 2.0
            self.lp = 2.0

        #allows access to and setting of boss's stats     
        def getHP(self):
            return int(self.hpp)
        def setHP(self, x):
            self.hpp = self.hpp + x
            return self.hpp
        def getAE(self):
            return int(self.aep)
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
        #If the enemy is attacked, the enemy's hit points decrease
                self.hpp = self.hpp - randrange(1,11)
                return print(self.hpp)
        def edied(self):
        #If the enemy's hit points = 0, the enemy is dead
                if self.hpp <= 0:
                    return True
        
              
