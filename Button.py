from graphics import *

class Button:

    #A button is a labeled rectangle in a window. It is activated or deactivated with the
    # activate() and deactivate() methods. The clicked(p) method returns true if
    # the button is active and p is inside it.

    def __init__(self, win, center, width, height, label, color):
        # creates a rectangular button, eg:
        # qb = Button(myWin, centerPoint, width, heigth, 'Quit')

        w, h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.color = color
        self.rect.setFill(self.color)
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.activate()

    def clicked(self, p):
        # returns true if button active and p is inside

        return(self.active and
               self.xmin <= p.getX() <= self.xmax and
               self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        # returns the label string of this button.
        
        return self.label.getText()

    def setLabel(self, string):
        #sets the text for the label

        self.label = string
        return self.label.draw(win)

    def activate(self):
        # sets this button to 'active'.

        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        # sets this button to 'inactive'.

        self.label.setFill('darkgray')
        self.rect.setWidth(2)
        self.active = False
