#SAIHARAN TKINTER
#imports Tkinter
from tkinter import *

<<<<<<< HEAD
#Makes the Tkinter window
scar=Tk()

#inserts the image as a label
bgraw = PhotoImage(file="C:\\Users\\admin.000\\Desktop\\homepage.jpg")
bglabel = Label(image=bgraw)
bglabel.pack()                 



scar.mainloop()
=======
def tkintermain():
    scar=Tk()
    scar.title("S.Car")

    bgraw = PhotoImage(file="C:\\Users\\admin.000\\Desktop\\homepage.png")
    bglabel = Label(image=bgraw)
    bglabel.pack()                 

    seatframe=Frame(scar,height=355,width=320)
    drinkframe=Frame(scar,height=355,width=320)

    seatframe.lower()
    drinkframe.lower()

    seatbutton=Button(scar)
    seatbutton=Button(scar)


    seatframe.place(x=0,y=65)
    drinkframe.place(x=320,y=65)

    seatframe.bind("<Button-1>",seatbelt)
    drinkframe.bind("<Button-1>",drinking)


    scar.mainloop()

    

def seatbelt(event):
    print ("Seatbelt")

def drinking(event):
    print ("Drinking")

tkintermain()
>>>>>>> 281712e1ee65898256e8f19dda9d5723bcd34816
