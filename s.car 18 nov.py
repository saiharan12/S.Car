#!/usr/bin/env python

from tkinter import *
import time

global speed
speed=StringVar
global times
times=0
global thinkdrunkvar
thinkdrunkvar=StringVar
global thinkdrunk
thinkdrunk=StringVar
font1=("Verdana",10)
font2=("verdana",12)

global buttonusa
global buttonindia
global buttonrussia
global buttonchina
global buttonethiopia
global buttonbangladesh
global buttonuk
global buttonother

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
        havedrunk=StringVar
        havedrunk=str(drinkselstr.get())
        testdrink()

    def enddrink():
        
                buttonusa.lower()
                buttonindia.lower()
                buttonrussia.lower()
                buttonchina.lower()
                buttoneurope.lower()
                buttonethiopia.lower()
                buttonbangladesh.lower()
                buttonuk.lower()
                buttonother.lower()

                country=str(countrytk.get())

                if country == ('usa' or 'uk'):
                    legallimit = 0.08
                elif country ==('india' or 'russia'):
                    legallimit = 0.03
                elif country =='france':
                    legallimit = 0.05
                elif country == 'china':
                    legallimit = 0.02
                elif country == 'ethiopia':
                    legallimit = 100
                elif country == 'bangladesh':
                    legallimit = 0
                else:
                    legallimit = 0.05

                drinktypetk = Entry(drinkframe,text="What kind of drink did you have?(beer,wine\"b,w\" or liqour(80proof)\"\"")
                drinktypetk.place(x=50,y=200)
                
                drinktype=str(drinktypetk.get())
     
        

    def contdrink():
           global countrytk
           countrytk=StringVar()
        
           radiodrinky.lower()
           radiodrinkn.lower()
            
           def quitscar():
               scar.destroy()

           if thinkdrunk == 'no':
               drinklabel1=Label(text="Ordering taxi to take you home safely",font=font1,fg="white",bg=bgcolorb)
               drinklabel1.place(x=50,y=250)
               drinkquitbutton=Button(drinkframe,text="Quit",command=quitscar)
               drinkquitbutton.place(x=100,y=300)
               taxiOrder = True
           elif thinkdrunk=='yes':
                countrytk=StringVar()
                
                havedrunklabel.configure(text="Select the country",fg="White")
                havedrunklabel.place(x=50,y=150)

                global buttonusa
                global buttonindia
                global buttonrussia
                global buttonchina
                global buttoneurope
                global buttonethiopia
                global buttonbangladesh
                global buttonuk
                global buttonother


                buttonusa=Radiobutton(drinkframe,text="USA",command=enddrink,bg=bgcolorb,fg="White",value="usa",variable=countrytk)
                buttonusa.place(x=50,y=280)
                buttonindia=Radiobutton(drinkframe,text="India",command=enddrink,bg=bgcolorb,fg="White",value="india",variable=countrytk)
                buttonindia.place(x=50,y=310)
                buttonrussia=Radiobutton(drinkframe,text="Russia",command=enddrink,bg=bgcolorb,fg="White",value="russia",variable=countrytk)
                buttonrussia.place(x=50,y=340)
                buttonchina=Radiobutton(drinkframe,text="China",command=enddrink,bg=bgcolorb,fg="White",value="china",variable=countrytk)
                buttonchina.place(x=50,y=370)
                buttoneurope=Radiobutton(drinkframe,text="Europe",command=enddrink,bg=bgcolorb,fg="White",value="europe",variable=countrytk)
                buttoneurope.place(x=150,y=280)
                buttonethiopia=Radiobutton(drinkframe,text="Ethiopia",command=enddrink,bg=bgcolorb,fg="White",value="ethiopia",variable=countrytk)
                buttonethiopia.place(x=150,y=310)
                buttonbangladesh=Radiobutton(drinkframe,text="Bangladesh",command=enddrink,bg=bgcolorb,fg="White",value="bangladesh",variable=countrytk)
                buttonbangladesh.place(x=150,y=340)
                buttonuk=Radiobutton(drinkframe,text="UK",command=enddrink,bg=bgcolorb,fg="White",value="uk",variable=countrytk)
                buttonuk.place(x=150,y=370)
                buttonother=Radiobutton(drinkframe,text="Others",command=enddrink,bg=bgcolorb,fg="White",value="other",variable=countrytk)
                buttonother.place(x=250,y=300)

    def testdrink():

        global thinkdrunkvar
        thinkdrunkvar=StringVar()

        def thinkdrunkexe():
            global thinkdrunk
            thinkdrunk=StringVar()
            thinkdrunk=str(thinkdrunkvar.get())
            contdrink()

        if havedrunk == 'yes':
           havedrunklabel.configure(text="Do you think you are sober enough to drive?")
           havedrunklabel.place(x=50,y=150)

           radiodrinky.configure(text="Yes",variable=thinkdrunkvar,value="yes",command=thinkdrunkexe)
           radiodrinky.place(x=50,y=180)

           radiodrinkn.configure(text="No",variable=thinkdrunkvar,value="no",command=thinkdrunkexe)
           radiodrinkn.place(x=260,y=180)

        else:
            print("Try this game")


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
    havedrunklabel.place(x=50,y=150)

    radiodrinky=Radiobutton(drinkframe,text="Yes",bg=bgcolorb,fg="white",font=10,value="yes",variable=drinkselstr,command=drinksel)
    radiodrinky.place(x=50,y=180)

    radiodrinkn=Radiobutton(drinkframe,text="No",bg=bgcolorb,fg="white",font=10,value="no",variable=drinkselstr,command=drinksel)
    radiodrinkn.place(x=200,y=180)

    seatlabel1=Label(seatframe)

    scar.mainloop()

tkintermain()
