import math
import random
import time
from tkinter import *
#top = tkinter.Tk()
#i'm starting now-eshan

caroff = False
stblt = False
speed = 0
brake = False
sx = 0
seatbeltbegintime = 0

print("Have a nice drive!")
print("The time and date is "+ str(time.ctime()))
inittime = str(time.ctime())

def speedreg(speedn):
    if speedn >= 120:
        print("SLOW DOWN: braking in...\n")
        for x in range(1,7):
            if x < 6:
                timercount = 6-x
                print(str(timercount)+ " seconds...")
                time.sleep(1)
                x = x+1
            else:
                brake = True
                print("Brake toggled\n")
                speed = 80
                print("Speed -> 80\n")
                break

def stopcar():
    print("Stopping Car\n")
    caroff = True

def seatbelt(speedn):
    stbltinput = input("enter the seatbelt state(on/off)\n")
    if stbltinput == "on":
        stblt = True
        seatbeltbegintime = time.time()
        print("drive safely!\n")
    elif stbltinput == "off":
        stblt = False
        if speedn >= 6:
            print("Please wear seatbelt. Braking in...\n")
            for y in range(1,7):
                if y < 6:
                    timercount = 6-y
                    print(str(timercount)+ " seconds...")
                    time.sleep(1)
                    y = y + 1

class display:
    #class for displaying crap - eshan
    #must run main before calling a display function
    # call these functions by using display.function(), print the result be
    def timerunning():
        timerunning ="this program has been running for "+ str(time.time()-realinittime)+" seconds"
        return timerunning
    def speed():
        # dispseed -> speed to display - eshan
        dispseed = "the speed is " +speed
        return dispspeed
    def brake():
        if brake == True:
            print("the brake is on")
        else:
            print("the brake is off")
    def carstate():
        if caroff == True:
            print("the car is off")
        else:
            print("the car is on")
    def stbltontime():
        dispstbltontime = "the stblt has been on for" + stbltontime
    def currenttime():
        print(str(ctime()))

def main():
    speed = input("Enter the speed of the vehicle in numerical format\n")
    speedn = int(speed)
    speedreg(speedn)
    seatbelt(speedn)
loop=1
while loop==1:
    main()
