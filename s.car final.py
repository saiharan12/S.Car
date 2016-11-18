#!/usr/bin/env python

from tkinter import *
import time
import random

global speed
speed=StringVar
global times
times=0
global thinkdrunkvar
thinkdrunkvar=StringVar
global thinkdrunk
thinkdrunk=StringVar
global drinktype
drinktype=StringVar
font1=("Verdana",10)
global taxiOrder
taxiOrder=bool

global buttonusa
global buttonindia
global buttonrussia
global buttonchina
global buttonethiopia
global buttonbangladesh
global buttonuk
global buttonother
global drinkamountentry
global genderbuttonm
global genderbuttonf
global weightentry
global confirmbutton
global bac
global wt
global legallimit
global ansentry
global queslabel
global testfor
global ncorrect
global usertest
global difficulty

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


    def drinkgame(ncorrect = 0):
       difficulty = 10
       incorrect = 0
       while ncorrect <= 5 or incorrect >= 10:
          testforA = random.randint(0,difficulty)
          testforB = random.randint(0,difficulty)
          if testforA or testforB == 0:
             testforA = random.randint(0,difficulty)
             testforB = random.randint(0,difficulty)

          testopchoose = random.randint(1,3)
          if testopchoose == 1:
                 testop = 'multiplied by'
                 testfor = testforA*testforB
                 while testforA>12 and testforB >12:
                        testforB = random.randint(0,difficulty)
                        testforA = random.randint(0,difficulty)
          elif testopchoose ==2:
                 testop = 'plus'
                 testfor = testforA+testforB
          elif testopchoose == 3:
                 testop = 'minus'
                 testfor = testforA-testforB
          while testfor < 0:
                testforB = random.randint(0,difficulty)
                testforA = random.randint(0,difficulty)
                testfor = testforA-testforB
          queslabel=Label(drinkframe,text=("What is  {} ".format(str(testforA))+testop+" {} ".format(str(testforB))),fg="white",bg=bgcolorb)
          queslabel.place(x=50,y=200)

          ansentry=Entry(drinkframe)
          ansentry.place(x=50,y=250)

          gameconfirm=Button(drinkframe,text="OK",fg="white",bg=bgcolorb,command=drinkgame2)
          gameconfirm.place(x=50,y=300)

          usertest=int(ansentry.get())

          if usertest == testfor:
             print("Correct")
             ncorrect = ncorrect+1
             difficulty = difficulty+5
             if ncorrect >= 5:
                 print("You have passed!")
          else:
             print("Wrong")
             difficulty += 10
             incorrect = incorrect+1
             if incorrect >=10:
                print("You have failed!")
                print("Ordering Taxi")
                taxiOrder = True



    def enddrink1():

        def enddrink2():

            def enddrink3():

                def enddrink4():

                    def enddrink5():

                        def enddrink6():

                            def enddrink7():

                                def enddrink8():

                                    def quitscarex():
                                        scar.destroy()

                                    confirmhours.lower()
                                    hoursdrink.lower()

                                    bac = ((sd/14)/wt*bw)*100
                                    if bac > legallimit:
                                        havedrunklabel.configure(text="You are too drunk to drive!")
                                        havedrunklabel.place(x=50,y=150)
                                        drinklabel3=Label(drinkframe,text="Ordering taxi",fg="white",bg=bgcolorb)
                                        drinklabel3.place(x=50,y=250)
                                        taxiOrder = True
                                        acbutton=Button(drinkframe,text="Quit",fg="white",bg=bgcolorb,command=quitscarex)
                                        acbutton.place(x=75,y=300)
                                    else:
                                        havedrunklabel.configure(text="Please answer the following questions to confirm")
                                        #drinkgame()

                                wt=int(weightentry.get())

                                confirmbutton.lower()
                                weightentry.lower()

                                havedrunklabel.configure(text="For how many hours were you drunk?")
                                havedrunklabel.place(x=50,y=150)

                                hoursdrink=Entry(drinkframe,fg="white",bg=bgcolorb)
                                hoursdrink.place(x=50,y=180)

                                confirmhours=Button(drinkframe,text="OK",fg="white",bg=bgcolorb,command=enddrink8)
                                confirmhours.place(x=70,y=210)


                            genderbuttonf.lower()
                            genderbuttonm.lower()

                            havedrunklabel.configure(text="Enter you weight(kgs)")
                            havedrunklabel.place(x=50,y=150)

                            weightentry=Entry(drinkframe,fg="white",bg=bgcolorb)
                            weightentry.place(x=50,y=180)

                            confirmbutton=Button(drinkframe,text="OK",command=enddrink7,fg="white",bg=bgcolorb)
                            confirmbutton.place(x=70,y=210)

                        global bw
                        global gender
                        gender=StringVar()
                        gender=gendertk.get()

                        bw=IntVar()
                        if gender=="m":
                            bw = 0.58
                        elif gender=="f":
                            bw = 0.49
                        enddrink6()


                    global gendertk
                    gendertk=StringVar()

                    drinkamountentry.lower()
                    drinkconfirm.lower()

                    havedrunklabel.configure(text="Select your gender")

                    genderbuttonm=Radiobutton(drinkframe,text="Male",value="m",variable=gendertk,command=enddrink5,fg="white",bg=bgcolorb)
                    genderbuttonm.place(x=50,y=200)
                    genderbuttonf=Radiobutton(drinkframe,text="Female",value="f",variable=gendertk,command=enddrink5,fg="white",bg=bgcolorb)
                    genderbuttonf.place(x=120,y=200)

                dam=float(drinkamountentry.get())

                drinktype=str(drinktypevar.get())

                if drinktype=='b':
                    dam=float(drinkamountentry.get())
                    sd = dam/12.0

                elif drinktype=='w':
                    dam=float(drinkamountentry.get())
                    sd = dam/5.0

                elif drinktype=='o':
                    dam=float(drinkamountentry.get())
                    sd = dam/1.5

                enddrink4()

            global drinkamountentry

            drinktypebuttonb.lower()
            drinktypebuttonw.lower()
            drinktypebuttono.lower()

            drinktype=drinktypevar.get()
            global drinklabel2
            drinklabel2=Label(drinkframe,fg="white",bg=bgcolorb)

            if drinktype == 'b':
                havedrunklabel.configure(text="How many cans or bottles did you drink?")
                havedrunklabel.place(x=50,y=150)

            elif drinktype == 'w':
                havedrunklabel.configure(text="How many ounces did you have?")
                havedrunklabel.place(x=50,y=150)

            elif drinktype == 'o':
                havedrunklabel.configure(text="How many shots did you have?")
                havedrunklabel.place(x=50,y=150)

            drinkconfirm=Button(drinkframe,text="OK",command=enddrink3,fg="white",bg=bgcolorb)
            drinkconfirm.place(x=200,y=200)

            drinkamountentry=Entry(drinkframe,fg="white",bg=bgcolorb)
            drinkamountentry.place(x=50,y=200)

        global drinktypevar
        drinktypevar=StringVar()

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

        havedrunklabel.configure(text="Select type of alcohol")

        drinktypebuttonb=Radiobutton(drinkframe,text="Beer",fg="white",bg=bgcolorb,command=enddrink2,value="b",variable=drinktypevar)
        drinktypebuttonb.place(x=50,y=200)
        drinktypebuttonw=Radiobutton(drinkframe,text="Wine",fg="white",bg=bgcolorb,command=enddrink2,value="w",variable=drinktypevar)
        drinktypebuttonw.place(x=100,y=200)
        drinktypebuttono=Radiobutton(drinkframe,text="Others",fg="white",bg=bgcolorb,command=enddrink2,value="o",variable=drinktypevar)
        drinktypebuttono.place(x=155,y=200)

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


            buttonusa=Radiobutton(drinkframe,text="USA",command=enddrink1,bg=bgcolorb,fg="White",value="usa",variable=countrytk)
            buttonusa.place(x=50,y=180)
            buttonindia=Radiobutton(drinkframe,text="India",command=enddrink1,bg=bgcolorb,fg="White",value="india",variable=countrytk)
            buttonindia.place(x=50,y=210)
            buttonrussia=Radiobutton(drinkframe,text="Russia",command=enddrink1,bg=bgcolorb,fg="White",value="russia",variable=countrytk)
            buttonrussia.place(x=50,y=240)
            buttonchina=Radiobutton(drinkframe,text="China",command=enddrink1,bg=bgcolorb,fg="White",value="china",variable=countrytk)
            buttonchina.place(x=50,y=270)
            buttoneurope=Radiobutton(drinkframe,text="Europe",command=enddrink1,bg=bgcolorb,fg="White",value="europe",variable=countrytk)
            buttoneurope.place(x=150,y=180)
            buttonethiopia=Radiobutton(drinkframe,text="Ethiopia",command=enddrink1,bg=bgcolorb,fg="White",value="ethiopia",variable=countrytk)
            buttonethiopia.place(x=150,y=210)
            buttonbangladesh=Radiobutton(drinkframe,text="Bangladesh",command=enddrink1,bg=bgcolorb,fg="White",value="bangladesh",variable=countrytk)
            buttonbangladesh.place(x=150,y=240)
            buttonuk=Radiobutton(drinkframe,text="UK",command=enddrink1,bg=bgcolorb,fg="White",value="uk",variable=countrytk)
            buttonuk.place(x=150,y=270)
            buttonother=Radiobutton(drinkframe,text="Others",command=enddrink1,bg=bgcolorb,fg="White",value="other",variable=countrytk)
            buttonother.place(x=100,y=300)

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

    speedentry=Entry(seatframe,bg=bgcolorg)
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
