# -*- coding: utf-8 -*-
import math
import random
import time
from tkinter import *
import sys
import select
import os

#top = tkinter.Tk()
#i'm starting now-eshan

def welcome():
   print("Welcome to S.car")
   time.sleep(1)

welcome()

caroff = False
stblt = False
speed = 0
brake = False
seatbeltbegintime = 0
drunk = False
TaxiOrder = False
mr = 0.017
wt = int(input("How much do you weigh?(kg) "))
gender = input("What is your gender?(m,f")
if gender == "m":
   bw = 0.58
elif gender == 'f':
   bw = 0.49
else:
   print("GTFO")


def __init__():
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
               print("\nBrake toggled")
               speed = 80
               print("Speed -> 80\n")
               break

def stopcar():
   print("Stopping Car\n")
   caroff = True

def seatbelt(speedn):
   stbltinput = input("enter the seatbelt state(on/off)\n")
   stbltinput = checkinput.seatbeltcheck(stbltinput)
   if stbltinput == "on":
       stblt = True
       seatbeltbegintime = time.time()
       print("drive safely!\n")
   elif stbltinput == "off":
       stblt = False
       if speedn >= 6:
           print("Please wear seatbelt. Braking in...\n")
           try:
              for y in range(1,11):
                  if y <= 11:
                      timercount = 11-y
                      print(str(timercount)+ " seconds...")
                      time.sleep(1)
                      y = y + 1
              print("Brake toggled\nSpeed ->5")
           except KeyboardInterrupt:
            print("Interrupted")
            pass
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

class checkinput:
   def speedcheck(speed):
      speednew = int(speed)
      while speednew>199 or speednew== 0:
         if speednew>199:
            print("please do not enter invalid values")
            speednew = int(input("please enter another value <199"))
         if speednew == 0:
            print("please do not enter null values")
            speednew = int(input("please enter another value"))
      return speednew
   
   def seatbeltcheck(onoff):
      if onoff == "on" or onoff == "off":
         pass
      else:
         print("please input a valid response(\"on\" or \"off\")\n")
         nstbltinput = input("input")
         return nstbltinput
   
def drinkgame():
   difficulty = 10
   ncorrect = 5
   incorrect = 0
   while ncorrect >= 5 or incorrect >= 10:
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
      else:
         pass
            
        
      usertest = int(input("What is  {} ".format(str(testforA))+testop+" {} ".format(str(testforB))))
      if usertest == testfor:
         print("correct")
         ncorrect = ncorrect-1
         difficulty = difficulty+5
         if ncorrect >= 5:
             print("you passed")
             break
      else:
         print("Wrong")
         difficulty += 10
         incorrect = incorrect+1
         if incorrect >=10:
            print("you failed")
            print("ordering Taxi")
            taxiOrder = True

   
         
  
   
     
      
def drinkreg():
   havedrunk = input("have you drank any alcohol?")
   if havedrunk == 'yes':
      thinkdrunk = input("do you think you are sober enough to drive?")
      if thinkdrunk == 'no':
         return ("ordering Taxi")
         taxiOrder = True
         return 0
      else:
         drinktype = input("what kind of drink did you have?(beer,wine\"b,w\" or liqour(80proof)\"\"")
         if drinktype == 'b':
                    dab = int(input("How many cans or bottles did you take?"))
                    sd = dab/12
            
         elif drinktype == 'w':
            daw = int(input("How many ounces did you take?"))
            sd = daw/5
         else:
            dal = int(input("How many shots did you take?"))
            sd = dal/1.5
         dp = int(input("how long have you drunk over(hours)"))
         
         #widmark formula - eshan
         # sd drinks
         Ebac = (((0.806 *sd*1.2)/bw*wt)*mr*dp)*10
         if Ebac > 0.030:
            print("you are too drunk to drive")
            print("Ordering taxi")
            taxiOrder = True
         else:
            print("try this game")
            drinkgame()
         
               
                    
                    
         
   else:
      print("drive safely!")
      


def main():
   speed = input("Enter the speed of the vehicle in numerical format\n")
   speed = checkinput.speedcheck(speed)
   speedn = int(speed) 
   speedreg(speedn)
   seatbelt(speedn)
   drinkreg()
loop=1
while loop==1:
   main
   if TaxiOrder:
      break
   if caroff:
      break
   

  

