import math
import random
import time
import tkinter
#top = tkinter.Tk()
#i'm starting now-eshan
def welcome():
    print("welcome to S.car")
    time.sleep(1)

welcome()

caroff = False
stblt = False
speedcalc = input("input the speed of the vehicle")
speed = int(speedcalc)
realinittime = time.time()
brake = False

seatbeltbegintime = 0
var = 1
def init():
    print("Have a nice drive!")
    print("the time and date is "+ str(time.ctime()))
    sx = 0
    inittime = str(time.ctime())
def speedreg():
    speed = int(speedcalc)
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
    stbltinput = input("enter the seatbelt state(on/off)")
    if stbltinput == "on":
        stblt = True
        seatbeltbegintime = time.time()
        print("drive safely!")
        
    elif stbltinput == "off":
        stblt = False
        if speed < 6:
            print("Drive slowly!")
            return 0
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
    speedreg()
    init()
    seatbelt()
    stbltontime = seatbeltbegintime - time.time()
    
    
main()       


    

