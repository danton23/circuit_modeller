from graphics import *
import math
import win32api  #REALLY useful (install with pip install PyWin32 but import as win32api) allows WIndows style alert boxes
Volt=0
Amp=0
Ohm=0
win = GraphWin(width = 600, height = 600) # create a window
win.setCoords(0, 0, 10, 10) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)
def valuecheck(window,x,y,z, *kwargs):
    argstring = []
    userinput=Entry(Point(x,y),z) #need to redefine it here or it 'redraws it' but retains previously entered value
    userinput.draw(window)
    window.getMouse()
    for arg in kwargs:
        if arg == int :
            argstring.append("integer")
        if arg ==str:
            argstring.append("word")
        if arg==float:
            argstring.append("float")
           
    for arg in kwargs:    
        try:
            assignedval=arg(userinput.getText())
            userinput.undraw()
            return assignedval
        except:      #This line tells loop to move on to next iteration (i.e next arg in kwargs according to FOR condition)
            pass
    else:    #This line (which lines up with FOR loop - i.e once all conditions in try loop have been FAILED - tells program to exectue win32 warning to tell user to input appropriate value
            argslist = []
            print(argslist)
            win32api.MessageBox(0, "Please select and appropriate value - must be " + str(' or '.join(argstring)), "Incorrect Entry")  #here str(','.join(argstring)) takes all items in list and prints them neatley (i.e without "" around and no [])
            userinput.undraw()
            return valuecheck(window,x,y,z, *kwargs)                                  #NOTE above i replaced ", " with "or" as the SEPERATOR so now says Integer OR string instead of Integer, String
  
label=Text(Point(5,1),"input source voltage")
label.draw(win)
Square2=Rectangle(Point(3.5,3.5), Point (4.5,2.5))# draw it to the window
Square2.setFill("red")
Square2.draw(win)
voltage = valuecheck(win, 4,2,5, int,float)
label.undraw()
Squarelab=Text(Point (4,2), str(voltage) + " V")
Squarelab.draw(win)
rlabel=Text(Point(8,9),"input resistance")
rlabel.draw(win)
resistance=valuecheck (win,7,8.5,5, float, int)
rlabel.undraw()
#label=Text(Point(8,9),"input current")
#label.draw(win)
#textEntry=Entry(Point(8,8),5)
#textEntry.draw(win)
#win.getMouse()
#current=textEntry.getText()
#label.undraw()
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
    Capacitance=valuecheck(win, 4, 0.5, 5, int, float)
    Caplabel2=Text(Point (5, 6), str(Capacitance) +" uF")
    Caplabel2.draw(win)
    Capchoice.undraw()
    Indchoice=Text(Point(4,1),"choose Inductor value!(mH)")
    Indchoice.draw(win)
    Inductance=valuecheck(win, 4, 0.5, 5, int, float)
    Indlabel2=Text(Point(0.5,6), str(Inductance)+"mH")
    Indlabel2.draw(win)
    Indchoice.undraw()
    CapInd=Capacitance*Inductance*10**-6
    RootCI=math.sqrt(CapInd)
    Resonantfreq=1/2*math.pi*RootCI
    print("resonant freq is " + str(Resonantfreq))
    Cap=Rectangle(Point(3.5,5.5),Point (4.5,6.5))# first pair of vals = position of lower LEFT corner, second = pos of lower RIGHT
    Cap.setFill("yellow")
    Cap.draw(win)
    Inductor=Rectangle(Point(1.5, 5.5), Point (2.5, 6.5))
    Inductor.setFill("blue")
    Inductor.draw(win)
    Userchoice=Text(Point(5,9), "Do you want to change values?")
    Userchoice.draw(win)
    Induse=Inductance/1000
    Usecap=Capacitance*10**-6
    resfreqprep=2*math.pi*math.sqrt(Induse*Usecap)
    resfreq=1/resfreqprep
    resfreqmhzs=resfreq/1000000
    resonanceLabel=Text(Point(4,4.25),"resonant frequency: " +str(resfreqmhzs) +" MHzs")
    resonanceLabel.draw(win)
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
            resonanceLabel.undraw()
            Inductor.undraw()
            Userchoice.undraw()
            Caplabel2.undraw()
            Indlabel2.undraw()
            Capchoice.undraw()
            Oscillator()
        elif choice == "no" or choice == "n":
            Userchoice.undraw()
            Userentry.undraw()
            
        else:
            win32api.MessageBox(0, "Please choose either y(es) or n(o)","Incorrect Entry")
            Userentry.undraw()
            Choice()
    Choice()
            
        

    #Inductor=
    
Oscillator()
def Antenna():
        print("test")
        def Antchoice():
        #data taken from http://www.antenna-theory.com/basics/bandwidth.php
             Antwin = GraphWin(title="Antenna types", width = 500, height = 500) # create a window
             Antwin.setCoords(0, 0, 10, 10)
             Windlabel=Text(Point (5, 9.5), "Antenna types")
             Windlabel.setStyle('bold')
             Windlabel.draw(Antwin)
             Patchlabel=Text(Point(5,8.5), "Patch - Center Freq:1000MHz, Freq Range:985-1015Mhz")
             Dilabel=Text(Point(5,6.5), "Dipole - Center Freq:1000MHz, Freq Range: 960-1040Mhz")
             Hornlabel=Text(Point(5,4.5),"Horn - Center Freq:10000Mhz, Freq Range:154-1848Mhz")
             Spirallabel=Text(Point(5, 2.5), "Spiral - Center Freq:1000Mhz, Freq Range: 95-1900MHz")
             Patchlabel.draw(Antwin)
             Dilabel.draw(Antwin)
             Hornlabel.draw(Antwin)
             Spirallabel.draw(Antwin)
             Choicelabel=Text(Point(5, 1), "Please choose an Antenna type - \"Patch\", \"Dipole\", \"Horn\", \"Spiral\"")
             Choicelabel.setFace("arial")
             Choicelabel.setStyle("italic")
             Userentry=Entry(Point(5,0.25),10)
             Userentry.draw(Antwin)
             Choicelabel.draw(Antwin)
             Antwin.getMouse()
             choice=Userentry.getText()
             choices=( "Patch","Dipole", "Horn", "Spiral")
             Anthighs=(1015, 1040, 1848, 1900)
             Antlows=(985, 960, 154, 95)
             if choice in choices:
                        for idx, val in enumerate(choices):   #REALLY useful function (enumerate(list)) enables you to get INDEX of item from a list - can then be used to extract OTHER values from other lists with same index!
                            if val==choice:
                                print(idx)
                                i=idx
                        print(i)
                        Antwin.close()
                        Anttype=choice
                        AntCentFreq=1000
                        Antlow=Antlows[i]
                        Anthigh=Anthighs[i]
                        Antlabel=Text(Point(2.5, 9.9),Anttype + ": "+ str(Antlow)+" Mhz - "+str(Anthigh) +" Mhz")
                        Antlabel.draw(win)
                        return Anttype, AntCentFreq, Antlow, Anthigh
          #   elif choice == "Dipole":
           #           Antwin.close()
            #          Anttype="Dipole"
             #         AntCentFreq=1000
              #        Antlow=960
              #       Anthigh=1040
                #      Antlabel=(Point(2.5, 9.9), "Dipole: "+ str(Antlow)+" Mhz - "+str(Anthigh) + " Mhz")
                 #     Antlabel.draw(win)
             else:
                        win32api.MessageBox(0, 'Please choose a valid option', 'Incorrect Entry')
                        Antwin.close()
                      
                        return Antchoice()   #VVVV IMPORTANT!!! if your function is supposed to be passing OUT vals to wider scope (as here with antype, center freq etc) then if you have failed loop (i.e else condition or something) which RE-CALLS function it is in MUST PUT RETURN in front to stop this returning NONE to wider scope when fails first time around! 
            
        Anttype, AntCentfreq, Antlow, Anthigh=Antchoice()
        Wire=Line (Point (2, 7), Point(2, 9.5))
        Wire.draw(win)
        Wire2=Line(Point(1.5,9.5), Point (2.5,9.5))
        Wire2.draw(win)
        Wire3=Line(Point(1,9.7), Point(3, 9.7))
        Wire3.draw(win)
        return Anttype, AntCentfreq, Antlow, Anthigh   #RETURN means when function is called will return these values - in order to use them out of its scope, however, must call func and also provide new (or same named) vals for returned vals to be passed into - see below
        
        
Anttype, AntCentfreq, Antlow, Anthigh = Antenna() #here we want BOTH to call func and for it to do what it normally does and THEN to store returned vals in outside scope, to do this we must FIRST name vals for returned vals to be stored in (in this case same as those they were 'passed out' in) and THEN call func 
def Transmit():
     Transwin = GraphWin(title="Choose a Frequency to transmit on", width = 500, height = 500) # create a window
     Transwin.setCoords(0, 0, 10, 10)
     def Centfreq():
       CentLab=Text(Point(5, 8), "Choose center Frequency (MHzs)")
       CentLab.draw(Transwin)
       centerentry=valuecheck(Transwin,5,7.5,5, int, float)
       if centerentry >=Antlow and centerentry<= Anthigh:
             print(Anttype + "Antype")
             TransCent=centerentry
             CentLab.undraw()
             CentLab2=Text(Point(5, 8), "Choose Transmission type (\"AM: 10Khz Bandwidth \", FM: varying Bandwidth \")")
             CentLab2.draw(Transwin)
             
             def AMFM():
               CentEnt=Entry(Point(5, 7.5),5)
               
               CentEnt.draw(Transwin)
               Transwin.getMouse()
               Userentry=CentEnt.getText()
               if Userentry=="AM":
                   Transwin.close()
                   FrequencyDev=10
                   return Userentry,FrequencyDev, TransCent
               elif Userentry=="FM":
                    print("Useentry=FM")
                    Transwin.close()
                    FMwin=GraphWin(title="Select Modulation Characteristics", width=500, height=500)
                    FMwin.setCoords(0,0,10,10)
                    FMlab=Text(Point(5,8), "Choose Frequency Deviation")
                    FMlab.draw(FMwin)
                    
                    def Freqcheck():
                      print("freqcheck")
                      FMEntry=Entry(Point(5, 7.5),5)
                      FMEntry.draw(FMwin)
                      FMwin.getMouse()
                      try:FrequencyDev=int(FMEntry.getText())
                      except:
                             win32api.MessageBox(0, "must be a number!", "incorrect entry")
                             return Freqcheck() 
                      if FrequencyDev >= 100 or FrequencyDev <= 50:
                          win32api.MessageBox(0, "Frequency deviation too high/low: Please choose a value between 50 and 100 KHZs")
                          FMEntry.undraw()
                          return Freqcheck()
                          
                        
                        
                      else:
                          FMwin.close()
                          return Userentry,FrequencyDev, TransCent
                    return Freqcheck()  
               else:
                        win32api.MessageBox(0, "Please choose Either AM or FM")
                        CentEnt.undraw()
                        return AMFM()   #HERE only works with 'return' keyword in front- otherwise means first time func is called below (Userentry,FrequencyDev, TransCent = Transmit()) it will return NONE and thus no values can be stored and prog will crash!
             return AMFM()
       else:
                win32api.MessageBox(0, "Frequency out of range for "+ Anttype + " type antenna, please choose a value between " + str(Antlow) + " and " + str(Anthigh) + " MHzs", "Alert")
                CentLab.undraw()
                return Centfreq()
                #Choice()
                #FrequencyDev, TransCent = Choice()
                ####CHANGE THIS!!! TO ALLOW LOOPING BEHVAIOUR WITHOUT CRASHING TRANSMIT (RETURNING "NONE" TYPE)
                
       
               # return Userentry, FrequencyDev, TransCent
     return Centfreq()
Userentry,FrequencyDev, TransCent = Transmit()
print(FrequencyDev)
print(TransCent)
print("Frequency Center = " + str(TransCent)+ " KHzs "+"Deviation = " + str(FrequencyDev)+ " KHzs")
Freqlow=TransCent - FrequencyDev
Freqhigh=TransCent + FrequencyDev
print("USB = " + str(Freqhigh)+ " LSB = " + str(Freqlow))
TransLabel=Text(Point(4.5,9),Userentry + " signal received on " + str(TransCent) +" MHzs " + "\n bandwidth:+- " + str(FrequencyDev)+" Khzs")
TransLabel.draw(win)
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
