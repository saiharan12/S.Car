import math
import random
import time
import tkinter
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

def speedreg():
    speed = input("Enter the speed of the vehicle in numerical format\n")
    speed = int(speed)
    if speed >= 120:
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
    
def seatbelt():
    stbltinput = input("enter the seatbelt state(on/off)\n")
    if stbltinput == "on":
        stblt = True
        seatbeltbegintime = time.time()
        print("drive safely!\n")
    elif stbltinput == "off":
        stblt = False
        if speed >= 6:
            print("Please wear seatbelt. Braking in...\n")
            for y in range(1,7):
                if y < 6:
                    timercount = 6-y
                    print(str(timercount)+ " seconds...")
                    time.sleep(1)
                    y = y + 1
        
    elif stbltinput == "off":
        stblt = False
        if speed < 6:
            print("Drive slowly!\n")
            return 0

def main():
    speedreg()
    seatbelt()

main()

