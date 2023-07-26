# THIS IS SMARTPHONE CLASS
class Smartphone:
    def __init__(self, brnd, clr, batt, aud, res, blt):
        self.brand = brnd
        self.color = clr
        self.battery = batt
        self.audio = aud
        self.resolution = res
        self.bluetooth = blt
        
# METHOD OF SMARTPHONE CLASS
# change and edit method
    def give_brand(self, brnd):
        self.brand = "Semsung"
        
    def give_color(self, clr):
        self.color = "Blue"
        
    def percent_battery(self):
# change the number and/or change the sign to - or +
        self.battery = self.battery + 3
        
    def mute_audio(self):
        self.audio = 1
# >=1 is equal to "No" and <1 is equal to "Yes"
    
    def change_resolution(self):
        self.resolution = "3840 x 2160"
        
    def connect_bluetooth(self):
        self.bluetooth = 1
# >=1 is equivalent to "Bluetooth on" and <1 is equivalent to "bluetooth off"

# MAIN PROGRAM
# default Smartphone attributes
mySmartphone = Smartphone("Semsung", "Red", 50, 0, "360 x 800", 0)

# Printed code
print ("1. My Smartphone")
print ("  Brand: " + mySmartphone.brand)
print ("  Color: " + mySmartphone.color)
print ("  Battery (before): ",mySmartphone.battery, "%")
mySmartphone.percent_battery()
print ("  Battery (after): ",mySmartphone.battery, "%")
# Below is the if-else statement that will return a string instead of the integer indicated in the mute_audio method. 
mySmartphone.mute_audio()
if mySmartphone.audio < 1:
    print ("  Mute: Yes")
else:
    print ("  Mute: No")
print ("  Resolution (before): " + mySmartphone.resolution + " pixels")
mySmartphone.change_resolution()
print ("  Resolution (after): " + mySmartphone.resolution + " pixels")
if mySmartphone.bluetooth < 1:
    print ("  Bluetooth: Off")
else:
    print ("  Bluetooth: On")
# Line space
print (" ")

# THIS IS THE EARPHONE CLASS
class Earphone:
    def __init__(self, brnd,clr, blt, batt, vol, call):
        self.brand = brnd
        self.color = clr
        self.bluetooth = blt
        self.battery = batt
        self.volume = vol
        self.call = call
        
# METHOD OF EARPHONE CLASS
    def give_brand(self,n):
        self.brand = n
        
    def give_color(self,n):
        self.color = n
        
    def connect_bluetooth(self):
# >=1 is equal to "Bluetooth on" and <1 is equal to "bluetooth off"
        self.bluetooth = 1
        
    def percent_battery(self,n):
# change the number and/or change the sign to - or +
        self.battery = self.battery + n
        
    def audio_volume(self,n):
        self.volume = n
        
    def answer_call(self,n):
# 'answer_call' refers to the feature of the earphone to answer/end/reject incoming calls.
        self.call = n
#The equivalence of the integers are: 1 = "answer call"; 2 = "reject call"; 3 = "end call"


# MAIN PROGRAM
# default attributes
myEarphone = Earphone("Semsung", "Black", 0, 80, 50, 1)

#Printed Code
print ("2. My Earphone")
print ("  Brand (before): " + myEarphone.brand)
myEarphone.give_brand("Orange")
print ("  Brand (after): " + myEarphone.brand)
print ("  Color: " + myEarphone.color)
# Below is the if-else statement that will return a string instead of the integer indicated in the connect_bluetooth method. 
if myEarphone.bluetooth >= 1:
    print ("  Bluetooth: On")
else:
    print ("  Bluetooth: Off")
print ("  Battery (before): ", myEarphone.battery, "%")
myEarphone.percent_battery(2)
print ("  Battery (after): ", myEarphone.battery, "%")
print ("  Volume (before): ", myEarphone.volume, "%")
myEarphone.audio_volume(100)
print ("  Volume (after): ", myEarphone.volume, "%")
# Below is the if-else-if statement that will return a string instead of the integer indicated in the answer_call method
myEarphone.answer_call(2)
if myEarphone.call == 1:
    print ("  Call: Answer")
elif myEarphone.call == 2:
    print ("  Call: Reject")
elif myEarphone.call == 3:
    print ("  Call: End")
else:
    print ("  Call: End")
print (" ")


# THIS IS THE STANDFAN cLASS
class Standfan:
    def __init__(self, brnd, clr, hgt, tlt, spd):
        self.brand = brnd
        self.color = clr
        self.height = hgt
        self.tilt = tlt
        self.speed = spd
# 'self.height' refers to the adjustable height standpipe feature and the 'self.tlt' refers to the tilting head feature of the standfan.

# METHOD OF STANDFAN CLASS
    def give_brand(self, n):
        self.brand = n
        
    def give_color(self, n):
        self.color = n
        
    def increase_height(self, n):
# 'increase_height' is adjusted by adding a number to the default(minimimum) height of the fan.
        self.height = self.height + n
        
    def tilt_head(self, n):
# 'tilt_head' refers to allowing the head to tilt side-to-side or not.
        self.tilt = n
# The equivalence of the integers are: 0 = "off" and 1 = "On"
    
    def change_speed(self, n):
# 'change_speed' refers to the speed of the fan as a feature of the standfan.
        self.speed = n        
# The equivalence of the integers are: 0 = "off"; 1 = "1x speed"; 2 = "2x speed"; 3 = "3x speed" """

# MAIN PROGRAM
# default attributes
myStandfan = Standfan("Eastern Appliances", "White", 36, 1, "off")

# Printed code
print ("3. My Standfan")
print ("  Brand: " + myStandfan.brand)
print ("  Color (before): " + myStandfan.color)
myStandfan.give_color("Black")
print ("  Color (after): " + myStandfan.color)
print ("  Height (before):", myStandfan.height, "inches")
myStandfan.increase_height(5)
print ("  Height (after):", myStandfan.height, "inches")
# Below is the if-else statement that will return a string instead of the integer indicated in the tilt_head method.
myStandfan.tilt_head(0)
if myStandfan.tilt == 1:
    print ("  Tilt Head: On")
else:
    print ("  Tilt Head: Off")
print ("  Speed/Power (before):", myStandfan.speed)
# Below is the if-else-if statement that will return a string instead of the integer indicated in the change_speed method 
myStandfan.change_speed(3)
if myStandfan.speed == 1:
    print ("  Speed/Power (after): 1")
elif myStandfan.speed == 2:
    print ("  Speed/Power (after): 2")
elif myStandfan.speed == 3:
    print ("  Speed/Power (after): 3")
else:
    print ("  Speed/Power (after): Off")
    






