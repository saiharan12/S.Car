from tkinter import *


def seatbelt(stbltinputtk):
    stbltinput=stbltinputtk.get()
    if stbltinput == "on":
       stblt = True
       seatbeltbegintime = time.time()
       drivesafely=Label(scarseat,text="Drive safely")
       drivesafely.place(x=420,y=420)
    elif stbltinput == "off":
       stblt = False
       if speedn >= 6:
           print("Please wear seatbelt. Braking in...\n")
           try:
              for y in range(1,11):
                  if y <= 11:
                      timercount = 11-y
                      timecounter=Label(scarseat,text=((str(timercount)+ " seconds...")))
                      timecounter.place(x=420,y=450)
                      time.sleep(1)
                      y = y + 1
           except KeyboardInterrupt:
            print("Interrupted")
            pass


def tkintermain():
    scar=Tk()
    scar.title("S.Car")

    seatframe=Frame(scar,height=640,width=480)
    drinkframe=Frame(scar,height=640,width=480)

    bgraw = PhotoImage(file="C:\\Users\\User\\Documents\\scar\\homepage.png")
    bglabel = Label(image=bgraw)
    bglabel.pack()

    bgrawseat = PhotoImage(file="C:\\Users\\User\\Documents\\scar\\seatbelt.png")
    bglabelseat = Label(seatframe,image=bgrawseat)

    bgrawdrink = PhotoImage(file="C:\\Users\\User\\Documents\\scar\\drinking.png")
    bglabeldrink = Label(drinkframe,image=bgrawdrink)

    seatframe.lower()
    drinkframe.lower()

    bgcolorg='#81C800'
    bgcolorb='#3F2904'
    
    seatbutton=Button(scar,text="Seatbelt",font="Verdana",fg="#FF0000",height=2,width=19,bg=bgcolorg,activebackground=bgcolorb)
    drinkbutton=Button(scar,text="Drinking",font="Verdana",fg="#FF0000",height=2,width=19,bg=bgcolorb,activebackground=bgcolorg)


    seatframe.place(x=0,y=65)
    drinkframe.place(x=320,y=65)

    seatbutton.place(x=60,y=340)
    drinkbutton.place(x=380,y=340)
    
    scar.mainloop()


tkintermain()

