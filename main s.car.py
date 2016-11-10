from tkinter import *
import time

def tkintermain():

    stbltinput = StringVar
    speed=int()

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
        print("executed")
        speedn=50
        stbltinput="off"

        if stbltinput == "on":
            print("works")
            stblt = True
            seatlabel1=Label(seatframe,text="Drive safely!")
            seatlabel1.place(x=380,y=440)

        elif stbltinput == "off":
           stblt = False
           if speedn >= 6:
               seatlabel1=Label(seatframe,text="Please wear seatbelt. Braking in...")
               seatlabel1.place(x=380,y=380)
               try:
                  for y in range(1,11):
                      if y <= 11:
                          timercount = 11-y
                          seatlabel2=Label(seatframe,text=str(timercount)+ " seconds...")
                          seatlabel2.place(x=430,y=400)
                          time.sleep(1)
                          y = y + 1
                  print("Brake toggled\nSpeed ->5")
               except KeyboardInterrupt:
                print("Interrupted")
                pass
    def testdrink():

        havedrunk=int
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

    bgraw = PhotoImage(file="C:\\Users\\admin.000\\Desktop\\homepage.png")
    bglabel = Label(image=bgraw)
    bglabel.pack()

    bgrawseat = PhotoImage(file="C:\\Users\\admin.000\\Desktop\\seatbelt.png")
    bglabelseat = Label(seatframe,image=bgrawseat)
    bglabelseat.pack()

    backseat=Button(seatframe,text="Homepage",command=goinghome)
    backseat.place(x=25,y=15)

    bgrawdrink = PhotoImage(file="C:\\Users\\admin.000\\Desktop\\seatbelt.png")
    bglabeldrink = Label(drinkframe,image=bgrawdrink)
    bglabeldrink.pack()

    backdrink=Button(drinkframe,text="Homepage",command=goinghome)
    backdrink.place(x=25,y=15)

    seatentry=Entry(seatframe,textvariable=stbltinput)
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

    speedentry=Entry(scar,textvariable=speed)
    speedentry.place(x=275,y=425)

    scar.mainloop()


tkintermain()
