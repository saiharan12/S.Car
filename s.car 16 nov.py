#!/usr/bin/env python

from tkinter import *
import time

speed=StringVar
global speed
times=0
global times

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

    def seatsel():
        global stbltinput
        stbltinput=StringVar()
        stbltinput=str(seatselstr.get())

    def drinksel():
        global havedrunk
        havedrunk=StringVar()
        havedrunk=str(drinkselstr.get())
        testdrink()

    def thinkdrunkexe():


    def testseat():

        speedtemp=speedentry.get()
        speedn=int(speedtemp)

        if stbltinput=="on":
            stblt = True
            seatlabel1.configure(text="Drive Safely!")
            seatlabel1.place(x=380,y=350)

        elif stbltinput == "off":
               stblt = False
               if speedn >= 6:
                   seatlabel1.configure(text="Please wear seatbelt. Braking in 10 seconds")
                   seatlabel1.place(x=360,y=350)
               else:
                    seatlabel1.configure(text="Parking mode on")
                    seatlabel1.place(x=360,y=350)

    def testdrink():

        global thinkdrunkvar
        thinkdrunkvar=StringVar()

        if havedrunk == 'yes':
           thinkdrunklabel = Label(drinkframe,text="Do you think you are sober enough to drive?")
           thinkdrunklabel.place(x=150,y=250)

           thinkdrunkradioy=Radiobutton(drinkframe,text="Yes",variable=thinkdrunkvar,value="yes",command=thinkdrunkexe).place(x=160,y=260)
           thinkdrunkradion=Radiobutton(drinkframe,text="No",variable=thinkdrunkvar,value="no").place(x=190,y=260)

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

    seatselstr=StringVar()
    drinkselstr=StringVar()
    bgcolorg='#81C800'
    bgcolorb='#3F2904'

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

    bgrawdrink = PhotoImage(file="drinking.png")
    bglabeldrink = Label(drinkframe,image=bgrawdrink)
    bglabeldrink.pack()

    backdrink=Button(drinkframe,text="Homepage",command=goinghome)
    backdrink.place(x=25,y=15)

    seattestbutton=Button(seatframe,text="Test",command=testseat,bg=bgcolorg)
    seattestbutton.place(x=445,y=280)

    seatframe.lower()
    drinkframe.lower()

    seatbutton=Button(scar,command=seatexe,text="Seatbelt",font="Verdana",fg="#FF0000",height=2,width=19,bg=bgcolorg,activebackground=bgcolorb)
    drinkbutton=Button(scar,command=drinkexe,text="Drinking",font="Verdana",fg="#FF0000",height=2,width=19,bg=bgcolorb,activebackground=bgcolorg)

    seatframe.place(x=0,y=65)
    drinkframe.place(x=320,y=65)

    seatbutton.place(x=60,y=340)
    drinkbutton.place(x=380,y=340)

    speedlabel=Label(seatframe,text="Enter speed",font="Verdana",bg=bgcolorg,fg="black")
    speedlabel.place(x=410,y=150)

    seatlabel2=Label(seatframe,text="Select status of the vehicle",font="Verdana",bg=bgcolorg,fg="black")
    seatlabel2.place(x=350,y=220)

    speedentry=Entry(seatframe)
    speedentry.place(x=400,y=180)

    radioseaty=Radiobutton(seatframe,text="Yes",bg=bgcolorg,font=10,value="on",variable=seatselstr,command=seatsel)
    radioseaty.place(x=390,y=250)

    radioseatn=Radiobutton(seatframe,text="No",bg=bgcolorg,font=10,value="off",variable=seatselstr,command=seatsel)
    radioseatn.place(x=485,y=250)

    havedrunklabel = Label(drinkframe,text="Have you drunk any alcohol?",bg=bgcolorb,fg="White",font=(12))
    havedrunklabel.place(x=100,y=150)

    radiodrinky=Radiobutton(drinkframe,text="Yes",bg=bgcolorb,fg="white",font=10,value="yes",variable=drinkselstr,command=drinksel)
    radiodrinky.place(x=100,y=180)

    radiodrinkn=Radiobutton(drinkframe,text="No",bg=bgcolorb,fg="white",font=10,value="no",variable=drinkselstr,command=drinksel)
    radiodrinkn.place(x=230,y=180)

    seatlabel1=Label(seatframe)

    scar.mainloop()

tkintermain()
