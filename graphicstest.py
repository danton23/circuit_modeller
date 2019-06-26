from graphics import *
import math
Volt=0
Amp=0
Ohm=0
win = GraphWin(width = 400, height = 400) # create a window
win.setCoords(0, 0, 10, 10) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)

label=Text(Point(5,1),"input source voltage")
label.draw(win)
textEntry = Entry(Point(4,2),5)
textEntry.draw(win)
Square2=Rectangle(Point(3.5,3.5), Point (4.5,2.5))# draw it to the window
Square2.setFill("red")
Square2.draw(win)
win.getMouse()

voltage = float(textEntry.getText())
label.undraw()
textEntry.undraw()
Squarelab=Text(Point (4,2), str(voltage) + " V")
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
y1=3.5
x2=4
y2=8
x3=8
y3=8
x4=8
y4=3
x5=4.5
y5=3
Wire=Line(Point(x1,y1), Point(x2, y2))
Wire2=Line(Point(x2, y2), Point(x3, y3))
Wire.draw(win)
Wire2.draw(win)

def Oscillator():
    subx1=4
    suby1=5
    subx2=2
    suby2=5
    subx3=2
    suby3=7
    subx4=4
    suby4=7

    
    SubWire1=Line(Point(subx1, suby1), Point(subx2, suby2))
    SubWire1.draw(win)
    SubWire2=Line(Point(subx2, suby2), Point(subx3, suby3))
    SubWire2.draw(win)
    SubWire3=Line(Point(subx3, suby3),Point(subx4, suby4))
    SubWire3.draw(win)
    Capchoice=Text(Point(4, 1), "choose Capacitor value!(uF)")
    Capchoice.draw(win)
    Capinput=Entry(Point(4, 0.5), 5)
    Capinput.draw(win)
    win.getMouse()
    Capacitance=float(Capinput.getText())
    Caplabel2=Text(Point (3, 3.75), str(Capacitance) +" uF")
    Caplabel2.draw(win)
    Capchoice.undraw()
    Capinput.undraw()
    Indchoice=Text(Point(4,1),"choose Inductor value!(mH)")
    Indchoice.draw(win)
    Indinput=Entry(Point(4,0.5),5)
    Indinput.draw(win)
    win.getMouse()
    Inductance=float(Indinput.getText())
    Indchoice.undraw()
    Indinput.undraw()
    Indlabel2=Text(Point(3,8), str(Inductance)+"mH")
    Indlabel2.draw(win)
    CapInd=Capacitance*Inductance*10**-6
    RootCI=math.sqrt(CapInd)
    Resonantfreq=1/2*math.pi*RootCI
    print("resonant freq is " + str(Resonantfreq))
    Cap=Rectangle(Point(2.5,4.5),Point (3.5,5.5))# first pair of vals = position of lower LEFT corner, second = pos of lower RIGHT
    Cap.setFill("yellow")
    Cap.draw(win)
    Inductor=Rectangle(Point(2.5, 6.5), Point (3.5, 7.5))
    Inductor.setFill("blue")
    Inductor.draw(win)
    Userchoice=Text(Point(5,9), "Do you want to change values?")
    Userchoice.draw(win)
    def Choice():
        Userentry=Entry(Point(5,8),5)
        Userentry.draw(win)
        win.getMouse()
        choice=Userentry.getText()
        if choice =="yes" or choice == "y":
            SubWire1.undraw()
            SubWire2.undraw()
            SubWire3.undraw()
            Cap.undraw()
            Inductor.undraw()
            Userchoice.undraw()
            Caplabel2.undraw()
            Indlabel2.undraw()
            Oscillator()
        elif choice == "no" or choice == "n":
            Userchoice.undraw()
            Userentry.undraw()
            
        else:
            print("Please choose yes or no")
    Choice()
            
        

    #Inductor=
    
Oscillator()  
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
