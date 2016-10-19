import math
import random
import time
import tkinter
#top = tkinter.Tk()
#this imports the tkinter module saiharan
# top.mainloop() makes a window
# http://www.tkdocs.com/tutorial/
#i'm starting now-eshan

caroff = False
stblt = False
speedcalc = input("Enter the speed of the vehicle in numerical format")
speed = int(speedcalc)
brake = False
sx = 0
def init():
    print("Have a nice drive!")
    print("the time and date is "+ str(time.ctime()))
    inittime = str(time.ctime())

def stopcar():
    print("Stopping Car")
    caroff = True
    
def seatbelt():
    stbltinput = input("enter the seatbelt state(on/off)")
    if stbltinput == "on":
        stblt = True
        seatbeltbegin = time.time()
        print("drive safely!")
        
    elif stbltinput == "off":
        stblt = False
        if speed > 120:
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
                    break
        else:
            if speed < 6:
                print("Drive slowly!")
                return 0
           
def main():
    stbltontime = time.time() - seatbeltbegin
    brake = True
            
seatbelt()

    

