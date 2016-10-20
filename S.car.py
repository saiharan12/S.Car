import math
import random
import time
<<<<<<< HEAD
import tkinter
#top = tkinter.Tk()
=======
#this imports the tkinter module saiharan
# top.mainloop() makes a window
# http://www.tkdocs.com/tutorial/
>>>>>>> origin/master
#i'm starting now-eshan

caroff = False
stblt = False

speed = "a"
brake = False
sx = 0
seatbeltbegintime = 0
var = 1
def init():
    print("Have a nice drive!")
    print("the time and date is "+ str(time.ctime()))
    inittime = str(time.ctime())
def speedreg(speed):
    print("enter the speed of the vehicle in numerical format")
    speed = int(speed)
    if speed >= 120:
            print("SLOW DOWN: braking in...")
            for x in range(1,7):
                if x < 6:
                    timercount = 6-x
                    print(str(timercount)+ " seconds...")
                    time.sleep(1)
                    x = x+1
                else:
                    brake = True
                    print("Brake toggled")
                    speed = 80
                    print("Speed -> 80")
                    break
        
def stopcar():
    print("Stopping Car")
    caroff = True
    
def seatbelt():
    stbltinput = input("Enter the seatbelt state(on/off)")
    if stbltinput == "on":
        stblt = True
<<<<<<< HEAD
        seatbeltbegintime = time.time()
        print("drive safely!")
        
    elif stbltinput == "off":
        stblt = False
        if speed < 6:
            print("Drive slowly!")
            return 0
           
def main():
    init()
    speedreg()
    seatbelt()
    stbltontime = time.time() - seatbeltbegintime
    
    
         
main()
 
=======
    elif stbltinput == "off":
        stblt = False
        now=time.time()
        if speed > 6:
            print("SLOW DOWN: braking in...")
            for x in range(1,7):
                if x > 5:
                    print("Car stopping...")
                    brake = True
                    print(str(x)+ " seconds...")
                    time.sleep(1)
                    x = x + 1
                else:
                    caroff = True
                    print("Stopping car...")

>>>>>>> origin/master

    

