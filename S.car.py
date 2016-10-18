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
def seatbelt():
    stbltinput = input("enter the seatbelt state(on/off)")
    if stbltinput == "on":
        stblt = True
        now = time.time()
        
    elif stbltinput == "off":
        stblt = False
        if speed < 6:
            print("SLOW DOWN: braking in...")
            for x in range(1,7):
                if x > 5:
                    print("Car stopping...")
                    brake = True
                    break
                print(str(x)+ " seconds...")
                time.sleep(1)
                x = x+1
                
        else:
            caroff = True
            print("Stopping car...")
#def main():
seatbelt()

    

