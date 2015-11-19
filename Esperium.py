#December 19, 2013
#This is a game called Esperium

import os
os.chdir('~/Documents/College1314/IntroComputer Science/esperium')

from graphics import *
from Button import *
from Playerclasses1 import *
from Enemyclasses1 import *

def characterchoose():
    #Create the window
    win = GraphWin("Choose Character", 1000, 800)
    win.setCoords(0,0,15,11)
    win.setBackground('lightgray')

    #Draw wizard box
    w = Button(win, Point(3, 7), 2.5, 2.5, "Wizard", 'lightblue')
    wtext = "A magic user who channels his arcane abilities in the form of fire and lighting. \nHe also has a pointy hat."
    
    #Draw fighter box
    f = Button(win, Point(7, 7), 2.5, 2.5, "Fighter", 'red')
    ftext = "A skilled martial combatant, who uses a sword and shield \nto smash his foes."
    
    #Draw archer box
    a = Button(win, Point(11, 7), 2.5, 2.5, "Archer", 'green')
    atext = "A woodsman who uses his bow and arrows to rain \ndeath and destruction on his foes."

    #Draw text box
    t = Rectangle(Point(1,1),Point(13,3))
    t.setFill('black')
    t.draw(win)

    #Set the text for the text box
    ttext = Text(Point(6.5,2),"Select a class to see a description.")
    ttext.setFill('white')
    ttext2 = Text(Point(6.5, 1.75), "Then choose your favorite and press ok.")
    ttext2.setFill('white')
    ttext3 = Text(Point(6.5, 1.5), "To quit, press quit.")
    ttext3.setFill('white')
    ttext.draw(win)
    ttext2.draw(win)
    ttext3.draw(win)

    #Draw quit button
    q = Button(win, Point(0.75, 10.25), 0.5, 0.5, "quit", 'darkgray')
    q.activate()

    #Draw the ok button
    o = Button(win, Point(14.25, 1.5), 0.5, 0.5, "OK", 'darkgray')
    o.activate()

    #Change the text in the text box based on which character the player chooses
    p = win.getMouse()
    while q.clicked(p) == False:
        if w.clicked(p) == True:
            ttext.setText(wtext)
            ttext2.setText("")
            ttext3.setText("")
        if f.clicked(p) == True:
            ttext.setText(ftext)
            ttext2.setText("")
            ttext3.setText("")
        if a.clicked(p) == True:
            ttext.setText(atext)
            ttext2.setText("")
            ttext3.setText("")
        p = win.getMouse()

    #Tell the game which character the player chose
        if o.clicked(p) == True:
            if ttext.getText() == wtext:
                player = wizard()
            elif ttext.getText() == ftext:
                player = fighter()
            else:
                player = archer()
            win.close()
            return player
            
    #Quit the game
    if q.clicked(p) == True:
            win.close()


def main():
    player = characterchoose()
    
    #Draws new window in which the rest of the game will take place
    win1 = GraphWin("Esperium", 1000, 800)
    win1.setCoords(0, 0, 15, 11)
    win1.setBackground('black')

    #Draws quit button
    q = Button(win1, Point(1, 10), 0.5, 0.5, "X", 'gray')
    
    #Draws character
    if player.getHP() == 30:
        pshape = Circle(Point(7.5, 2), 1)
        pshape.setFill('lightblue')
        pshape.draw(win1)
    elif player.getHP() == 50:
        pshape = Circle(Point(7.5, 2), 1)
        pshape.setFill('red')
        pshape.draw(win1)
    else:
        pshape = Circle(Point(7.5, 2), 1)
        pshape.setFill('green')
        pshape.draw(win1)

    #Creates text box for instructions
    textbox = Button(win1, Point(7.5, 6), 8, 2, "", 'gray')
    text = Text(Point(7.5, 6), "Ready yourself! Enemies approach! \n[Click here to continue]")
    text.draw(win1)

    #Creates and draws enemies
    enemy1 = enemy()
    enemy2 = enemy()
    enemy3 = enemy()

    e1 = Button(win1, Point(3, 8), 1.5, 1.5, "ORC 1", 'purple')
    e2 = Button(win1, Point(7, 8), 1.5, 1.5, "ORC 2", 'purple')
    e3 = Button(win1, Point(11, 8), 1.5, 1.5, "ORC 3", 'purple')

    p = win1.getMouse()

    if textbox.clicked(p):
        text.setText("Click an enemy to attack them")
        
    #COMBAT
    p = win1.getMouse()
    while not q.clicked(p):
        p = win1.getMouse()

        if e1.clicked(p):
            enemy1.attacked()
            text.setText("ORC 1 hit!")
            player.attacked()
            if player.edied():
                text.setText("You have died. Poor mortal. Click the 'X' to quit.")
            if enemy1.edied():
                e1.deactivate()
                text.setText("ORC 1 is dead!")
        elif e2.clicked(p):
            enemy2.attacked()
            text.setText("ORC 2 hit!")
            player.attacked()
            if player.edied():
                text.setText("You have died. Poor mortal. Click the 'X' to quit.")
            if enemy2.edied():
                e2.deactivate()
                text.setText("ORC 2 is dead!")
        elif e3.clicked(p):
            enemy3.attacked()
            text.setText("ORC 3 hit!")
            player.attacked()
            if player.edied():
                text.setText("You have died. Poor mortal. Click the 'X' to quit.")
            if enemy3.edied():
                e3.deactivate()
                text.setText("ORC 3 is dead!")
        elif q.clicked(p):
            win1.close()
        else:
            p = win1.getMouse()

        #BOSS BATTLE!
        if enemy1.edied() and enemy2.edied() and enemy3.edied():
            dragon = boss()
            b1 = Button(win1, Point(7.5, 9), 12, 3, "ELDER DRAGON", 'orange')
            player.setHP(25)
            text.setText("Your health has been restored!")
            p = win1.getMouse()
            while not q.clicked(p):
                if b1.clicked(p):
                    dragon.attacked()
                    text.setText("Elder Dragon hit!")
                    player.attacked()
                    if player.edied():
                        text.setText("You were roasted to a crisp. Click the 'X' to quit.")
                        b1.deactivate()
                    if dragon.edied():
                        b1.deactivate()
                        text.setText("You did it! You vanquished the beast! Dance for joy! \n[Click the 'X' to quit]")
                if q.clicked(p):
                    win1.close()
                p = win1.getMouse()
                
    win1.close()
        
main()
