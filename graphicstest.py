from graphics import *
Volt=0
Amp=0
Ohm=0
win = GraphWin(width = 400, height = 400) # create a window
win.setCoords(0, 0, 10, 10) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)

label=Text(Point(5,1),"input source voltage")
label.draw(win)
textEntry = Entry(Point(4,2),5)
textEntry.draw(win)
Square2=Rectangle(Point(4,4), Point (3,3))# draw it to the window
Square2.setFill("red")
Square2.draw(win)
win.getMouse()

voltage = float(textEntry.getText())
label.undraw()
textEntry.undraw()
Squarelab=Text(Point (2,3), str(voltage) + " V")
Squarelab.draw(win)
rlabel=Text(Point(8,9),"input resistance")
rlabel.draw(win)
rtextEntry=Entry(Point(7,8.5),5)
rtextEntry.draw(win)
win.getMouse()
resistance=float(rtextEntry.getText())
rlabel.undraw()
rtextEntry.undraw()
#label=Text(Point(8,9),"input current")
#label.draw(win)
#textEntry=Entry(Point(8,8),5)
#textEntry.draw(win)
#win.getMouse()
#current=textEntry.getText()
#label.undraw()
textEntry.undraw()


x1=4
y1=4
x2=4
y2=8
x3=8
y3=8
x4=8
y4=3
x5=3
y5=3
Wire=Line(Point(x1,y1), Point(x2, y2))
Wire2=Line(Point(x2, y2), Point(x3, y3))
Wire.draw(win)
Wire2.draw(win)
Wire3=Line(Point(x3,y3), Point (x4,y4))
Wire3.draw(win)
Square4=Rectangle(Point(7.5,4),Point(8.5,5))
Square4.setFill("green")
Square4.draw(win)
Square4Lab=Text(Point(6, 4.5),"Enter resistance")
Square4text=Entry(Point(6, 5),5)
Square4Lab.draw(win)
Square4text.draw(win)
Wire4=Line(Point(x4, y4), Point(x5, y5))
Wire4.draw(win)
Square3Lab=Text(Point(8,9.5),"L.E.D")
Square3Lab.draw(win)
Square3=Rectangle(Point(8,8), Point (9,9))
Square3.draw(win)
win.getMouse()
componentresistance=float(Square4text.getText())
Square4Lab.undraw()
Square4text.undraw()
ComRes=Text(Point(6,4.5), str(componentresistance)+ " Ohms")
ComRes.draw(win)
tr=componentresistance+resistance
ResLab=Text(Point(7, 8.5), str(resistance) +" Ohms")
ResLab.draw(win)
current=voltage/tr
currentlabel=Text(Point(6,2), str(current)+" A")
currentlabel.draw(win)
win.getMouse()# pause before closing
