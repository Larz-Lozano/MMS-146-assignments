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


# THIS IS THE STANDFAN CLASS
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
print ("")

#This is the Laptop Class
class Laptop:
    def __init__(self,brnd,batt,clr,bght,backkey,wgt,wdth,os):
        self.brand = brnd
        self.battery = batt
        self.color = clr
        self.brightness = bght
        self.backlit_keyboard = backkey
        self.weight = wgt
        self.width = wdth
        self.os = os

# METHOD FOR LAPTOP CLASS
    def give_brand(self,n):
        self.brand = n

    def give_color(self,n):
        self.color = self.color + n

    def percent_battery(self,n):
        self.battery = self.battery - n

    def increase_brightness(self, n):
        self.brightness = self.brightness + n

    def decrease_brightness(self, n):
        self.brightness = self.brightness - n

    def on_backlit_keyboard(self, n):
        self.backlit_keyboard = n

    def update_os(self,n):
        self.os = n + "(updated)"
        

#Main Program
myLaptop = Laptop("apple",100,"white",10,1,200,300,"MACOSN")

print ("4. My Laptop")
print ("  Brand: " + myLaptop.brand)
print ("  Battery (before):", myLaptop.battery, "%")
myLaptop.percent_battery(3)
print ("  Battery (after):", myLaptop.battery, "%")
print ("  Color: " + myLaptop.color)
print ("  OS (before): " + myLaptop.os)
myLaptop.update_os("MACOSX")
print ("  OS (after): " + myLaptop.os)
print ("  Brightness (before):", myLaptop.brightness, "%")
myLaptop.increase_brightness(5)
print ("  Brightness (after):", myLaptop.brightness, "%")
if myLaptop.backlit_keyboard >= 1:
    print ("  Backlit Keyboard: On")
else:
    print ("  Backlit Keyboard: Off")
print (" ")

# THIS IS BOOK CLASS
class Book:
    def __init__(self,ttl,aut,hgt,wgt,wdt,pg):
        self.title = ttl
        self.author = aut
        self.height = hgt
        self.weight = wgt
        self.width = wdt
        self.page = pg

# METHOD OF BOOK CLASS
    def give_title(self,n):
        self.title = n

    def name_author(self,n):
        self.author = n

    def give_height(self,n):
        self.height = n

    def give_weight(self,n):
        self.weight = n

    def give_width(self,n):
        self.width = n

    def next_page(self):
        self.page = self.page + 1

    def previous_page(self):
        self.page = self.page - 1

    def bookmarked_page(self,n):
        self.page = n

#Main Program
favBook = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 9.5, 600, 5, 300)

print ("5. Favorite Book")
print ("  Title: " + favBook.title)
print ("  Author: " + favBook.author)
print ("  Current Page:", favBook.page)
favBook.next_page()
print ("  Next Page:", favBook.page)
favBook.previous_page()
print ("  Previous Page:", favBook.page)
favBook.bookmarked_page(205)
print ("  Bookmarked Page:", favBook.page)
print (" ")

# THIS IS CABINET CLASS
class Cabinet:
    def __init__(self,clr,dr,clth,hgt,wdt,wgt):
        self.color = clr
        self.door = dr
        self.clothes = clth
        self.height = hgt
        self.width = wdt
        self.weight = wgt

#This is the methods for the Cabinet Class
    def give_color(self,n):
        self.color = n

    def lock_door(self,n):
        self.door = n

    def give_height(self,n):
        self.height = n

    def give_width(self,n):
        self.width = n

    def give_weight(self,n):
        self.weight = n

    def add_clothes(self, n):
        self.clothes = self.clothes + n

    def remove_clothes(self,n):
        self.clothes = self.clothes - n

#Main Program
Cabinet1 = Cabinet("Brown","Unlocked",5,10,30,80)

print ("6. My Cabinet")
print ("  Color:" + Cabinet1.color)
print ("  Height:", Cabinet1.height, "inches")
print ("  Weight:", Cabinet1.weight, "kilograms")
print ("  No. of Clothes:", Cabinet1.clothes)
Cabinet1.add_clothes(4)
print ("  No. of Clothes Added:", Cabinet1.clothes)
Cabinet1.remove_clothes(3)
print ("  No. of Clothes Removed:", Cabinet1.clothes)
print ("  Door (before):", Cabinet1.door)
Cabinet1.lock_door("Locked")
print ("  Door (after):", Cabinet1.door)   
print (" ")


#THIS IS WASHING MACHINE CLASS
class WashingMachine:
    def __init__(self,tmr,wtr,clr,ldry,prog):
        self.timer = tmr
        self.water = wtr
        self.color = clr
        self.laundry = ldry
        self.program = prog

#This is the methods for the Washing Machine Class
    def increase_timer(self):
        self.timer = self.timer + 5

    def add_water(self,n):
        self.water = self.water + n

    def drain_water(self,n):
        self.water = self.water - n

    def give_color(self,n):
        self.color = n

    def add_laundry(self,n):
        self.laundry = self.laundry + n

    def remove_laundry(self,n):
        self.laundry = self.laundry - n

    def wash_program(self,n):
        self.program = n
    
#Main Program
WashingMachine1 = WashingMachine(35,0,"blue",5, 2)


print ("7. Washing Machine")
print ("  Color: " + WashingMachine1.color)
print ("  Water (before):", WashingMachine1.water, "gallons")
WashingMachine1.add_water(6)
print ("  Water (after):", WashingMachine1.water, "gallons")
print ("  No. of Laundry (before):", WashingMachine1.laundry)
WashingMachine1.add_laundry(5)
print ("  No. of Laundry (after):", WashingMachine1.laundry)
if WashingMachine1.program ==1:
    WashingMachine1.program = "Gentle"
elif WashingMachine1.program == 2:
    WashingMachine1.program = "Normal"
elif WashingMachine1.program == 3:
    WashingMachine1.program = "Strong"
print ("  Wash Program: " + WashingMachine1.program)
print (" ")

#This is the Bed Class
class Bed:
    def __init__(self,clr,wdt,lth,bsht,plw,blkt):
        self.color = clr
        self.width = wdt
        self.length = lth
        self.bedsheet = bsht
        self.pillows = plw
        self.blanket = blkt

#This is the methods for the Bed Class
    def give_color(self,n):
        self.color = n

    def give_width(self,n):
        self.width = n

    def give_length(self,n):
        self.length = n

    def change_bedsheet(self,n):
        self.bedsheet = n

    def add_pillows(self,n):
        self.pillows = self.pillows + n

    def remove_pillows(self,n):
        self.pillows = self.pillows - n

    def change_blanket(self,n):
        self.blanket = n

#Main Program
myBed = Bed("Gray",500,150,"Black",2,"Pattern")

print ("8. My Bed")
print ("  Color: " + myBed.color)
print ("  Width:", myBed.width, "inches")
print ("  Length:", myBed.length, "inches")
print ("  Bedsheet (before): " + myBed.bedsheet)
myBed.change_bedsheet("White with Green Stripes")
print ("  Bedsheet (after): " + myBed.bedsheet)
print ("  Blanket (before): " + myBed.blanket)
myBed.change_blanket("Plain Green")
print ("  Blanket (after): ", myBed.blanket)
print ("  No. of Pillows (before):", myBed.pillows )
myBed.remove_pillows(1)
print ("  No. of Pillows (after):", myBed.pillows )
