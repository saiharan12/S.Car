#!/usr/bin/env python

from Tkinter import *
import time

stbltinput = StringVar
speed=StringVar
times=0

def tkintermain():

    def seatexe():
        seatframe.lift()
        seatframe.place(x=0,y=0)

    def drinkexe():
        drinkframe.lift()
        drinkframe.place(x=0,y=0)

    def goinghome():
        seatframe.lower()
        drinkframe.lower()

    def testseat():

        speedtemp=speedentry.get()
        speedn=int(speedtemp)

        stbltinput=seatentry.get()

        if stbltinput == "on":
            seatlabel1.lower()
            stblt = True
            seatlabel1=Label(seatframe,text="Drive safely!")
            seatlabel1.place(x=380,y=350)

        elif stbltinput == "off":
            seatlabel1.lower()
           stblt = False
           if speedn >= 6:
               seatlabel1=Label(seatframe,text="Please wear seatbelt. Braking in 10 seconds")
               seatlabel1.place(x=350,y=350)
               print("Brake toggled\nSpeed ->5")
           else:
                seatlabel2=Label(seatframe,text="Parking mode on")
                seatlabel2.place(x=500,y=430)

    def testdrink():

        havedrunk=StringVar
        havedrunklabel = Label(drinkframe,text="Have you drink any alcohol?")
        havedrunklabel.place(x=150,y=250)

        havedrunkentry=Entry(seatframe,textvariable=havedrunk)
        havedrunkbutton=Button(drinkframe,Text="OK",command=drinkrun)
        def drinkrun():
            if havedrunk == 'yes':
               thinkdrunk = input("Do you think you are sober enough to drive?")
               if thinkdrunk == 'no':
                   return ("Ordering Taxi to take you safely!")
                   taxiOrder = True
                   return 0
               else:
                   drinktype = input("What kind of drink did you have?(beer,wine\"b,w\" or liqour(80proof)\"\"")
                   if drinktype == 'b':
                       dab = int(input("How many cans or bottles did you drink?"))
                       sd = dab/12
                   elif drinktype == 'w':
                       daw = int(input("How many ounces did you have?"))
                       sd = daw/5
                   else:
                       dal = int(input("How many shots did you have?"))
                       sd = dal/1.5
                       dp = int(input("How long have you been drunk (hours)"))

                       Ebac = (((0.806 *sd*1.2)/bw*wt)*mr*dp)*10
                       if Ebac > 0.030:
                           print("You are too drunk to drive!")
                           print("Ordering taxi")
                           taxiOrder = True
            else:
                print("Try this game")



    def speedregtk():
        speed=speed.get()
        speedn=int(speed)

        return(speedn)

    scar=Tk()
    scar.title("S.Car")

    seatframe=Frame(scar,height=640,width=480)
    drinkframe=Frame(scar,height=640,width=480)

    bgraw = PhotoImage(file="homepage.png")
    bglabel = Label(image=bgraw)
    bglabel.pack()

    bgrawseat = PhotoImage(file="seatbelt.png")
    bglabelseat = Label(seatframe,image=bgrawseat)
    bglabelseat.pack()

    backseat=Button(seatframe,text="Homepage",command=goinghome)
    backseat.place(x=25,y=15)

    bgrawdrink = PhotoImage(file="seatbelt.png")
    bglabeldrink = Label(drinkframe,image=bgrawdrink)
    bglabeldrink.pack()

    backdrink=Button(drinkframe,text="Homepage",command=goinghome)
    backdrink.place(x=25,y=15)

    seatentry=Entry(seatframe)
    seatentry.place(x=400,y=250)

    seattestbutton=Button(seatframe,text="Test",command=testseat)
    seattestbutton.place(x=450,y=300)

    seatframe.lower()
    drinkframe.lower()

    bgcolorg='#81C800'
    bgcolorb='#3F2904'

    seatbutton=Button(scar,command=seatexe,text="Seatbelt",font="Verdana",fg="#FF0000",height=2,width=19,bg=bgcolorg,activebackground=bgcolorb)
    drinkbutton=Button(scar,command=drinkexe,text="Drinking",font="Verdana",fg="#FF0000",height=2,width=19,bg=bgcolorb,activebackground=bgcolorg)

    seatframe.place(x=0,y=65)
    drinkframe.place(x=320,y=65)

    seatbutton.place(x=60,y=340)
    drinkbutton.place(x=380,y=340)

    speedlabel=Label(scar,text="Enter speed",font="Verdana",bg="black",fg="white")
    speedlabel.place(x=150,y=420)

    speedentry=Entry(scar)
    speedentry.place(x=275,y=425)

    scar.mainloop()

tkintermain()
