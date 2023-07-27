print ("07/27/2023")
print ("MMS 146 - Assignment #2")
print ("Submitted by: Laryze Lozano and Jeremias Cotibar")
print ("")


# THIS IS THE SMARTPHONE CLASS ------------------------------
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
    def give_brand(self, n):
        self.brand = n
        
    def give_color(self, n):
        self.color = n
        
    def percent_battery(self,n):
        self.battery = self.battery + n
        
    def mute_audio(self):
# >=1 is equal to "No" and <1 is equal to "Yes"
        self.audio = 1
    
    def change_resolution(self,n):
        self.resolution = n
        
    def connect_bluetooth(self,n):
# >=1 is equivalent to "bluetooth on" and <1 is equivalent to "bluetooth off"
        self.bluetooth = n

# MAIN PROGRAM
# default Smartphone attributes
mySmartphone = Smartphone("Semsung", "Red", 50, 0, "360 x 800", 0)

# Printed code
print ("1. My Smartphone")
print ("  Brand: " + mySmartphone.brand)
print ("  Color: " + mySmartphone.color)
print ("  Battery (before): ",mySmartphone.battery, "%")
mySmartphone.percent_battery(3)
print ("  Battery (after): ",mySmartphone.battery, "%")
# Below is the if-else statement that will return a string instead of the integer indicated in the mySamrtphone.audio method. 
mySmartphone.mute_audio()
if mySmartphone.audio < 1:
    mySmartphone.audio = "Yes"
else:
    mySmartphone.audio = "No"
print ("  Mute: " + mySmartphone.audio)
print ("  Resolution (before): " + mySmartphone.resolution + " pixels")
mySmartphone.change_resolution("3840 x 2160")
print ("  Resolution (after): " + mySmartphone.resolution + " pixels")
if mySmartphone.bluetooth < 1:
    mySmartphone.bluetooth = "Off"
else:
    mySmartphone.bluetooth = "On"
print ("  Bluetooth: " + mySmartphone.bluetooth)
# Line space
print (" ")

# THIS IS THE EARPHONE CLASS --------------------------------
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
        self.battery = self.battery + n
        
    def audio_volume(self,n):
        self.volume = n
        
    def answer_call(self,n): #refers to the feature of the earphone to answer/end/reject incoming calls.
# 1 = "answer call"; 2 = "reject call"; 3 = "end call"
        self.call = n
        

# MAIN PROGRAM
# default attributes
myEarphone = Earphone("Semsung", "Black", 0, 80, 50, 1)

#Printed Code
print ("2. My Earphone")
print ("  Brand (before): " + myEarphone.brand)
myEarphone.give_brand("Orange")
print ("  Brand (after): " + myEarphone.brand)
print ("  Color: " + myEarphone.color)
# Below is the if-else statement that will return a string instead of the integer indicated in the myEarphone.bluetooth method. 
if myEarphone.bluetooth >= 1:
    myEarphone.bluetooth = "On"
else:
    myEarphone.bluetooth = "Off"
print ("  Bluetooth: " + myEarphone.bluetooth)
print ("  Battery (before):", myEarphone.battery, "%")
myEarphone.percent_battery(2)
print ("  Battery (after):", myEarphone.battery, "%")
print ("  Volume (before):", myEarphone.volume, "%")
myEarphone.audio_volume(100)
print ("  Volume (after):", myEarphone.volume, "%")
# Below is the if-else-if statement that will return a string instead of the integer indicated in the myEarphone.call attribute
myEarphone.answer_call(2)
if myEarphone.call == 1:
    myEarphone.call = "Answer"
elif myEarphone.call == 2:
    myEarphone.call = "Reject"
elif myEarphone.call == 3:
    myEarphone.call = "End"
else:
    myEarphone.call = "End"
print ("  Calls: " + myEarphone.call)
print (" ")


# THIS IS THE STANDFAN CLASS --------------------------------
class Standfan:
    def __init__(self, brnd, clr, hgt, tlt, spd):
        self.brand = brnd
        self.color = clr
        self.height = hgt #refers to the adjustable height standpipe feature 
        self.tilt = tlt #refers to the tilting head feature of the standfan.
        self.speed = spd


# METHOD OF STANDFAN CLASS
    def give_brand(self, n):
        self.brand = n
        
    def give_color(self, n):
        self.color = n
        
    def increase_height(self, n): # 'increase_height' is adjusted by adding a number to the default(minimimum) height of the fan.
        self.height = self.height + n
        
    def tilt_head(self, n): # 'tilt_head' refers to allowing the head to tilt side-to-side or not.
  # 0 = "off" and 1 = "On"
        self.tilt = n
    
    def change_speed(self, n):
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
# Below is the if-else statement that will return a string instead of the integer indicated in the myStandfan.tilt attribute.
myStandfan.tilt_head(0)
if myStandfan.tilt == 1:
   myStandfan.tilt = "On"
elif myStandfan.tilt == 0:
    myStandfan.tilt= "Off"
else:
     myStandfan.tilt= "Off"
print ("  Tilt: " + myStandfan.tilt)
print ("  Speed/Power (before):", myStandfan.speed)
# Below is the if-else-if statement that will return a string instead of the integer indicated in the myStandfan.speed attribute 
myStandfan.change_speed(3)
if myStandfan.speed <= 0:
    myStandfan.speed = "Off"
else:
    myStandfan.speed = myStandfan.speed
print ("  Speed/Power (after):", myStandfan.speed)
print (" ")

# THIS IS THE LAPTOP CLASS ----------------------------------
class Laptop:
    def __init__(self,brnd,batt,clr,bght,backkey,wgt,wdth,os):
        self.brand = brnd
        self.battery = batt
        self.color = clr
        self.brightness = bght
        self.backlit_keyboard = backkey #refers to the led light of the keyboard
        self.weight = wgt
        self.width = wdth
        self.os = os #operating system

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

    def update_os(self,n): #refers to the updated operating system
        self.os = n + "(updated)"
        

# MAIN PROGRAM
# default attributes
myLaptop = Laptop("Epple",100,"White",10,1,200,300,"MACOSN")

# Printed code
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
# Below is the if-else-if statement that will return a string instead of the integer indicated in the myLaptop.backlit_keyboard attribute 
if myLaptop.backlit_keyboard >= 1:
    print ("  Backlit Keyboard: On")
else:
    print ("  Backlit Keyboard: Off")
print (" ")

# THIS IS THE BOOK CLASS ------------------------------------ 
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

# MAIN PROGRAM
# default attributes
favBook = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 9.5, 600, 5, 300)

# Printed code
print ("5. My Favorite Book")
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

# THIS IS THE CABINET CLASS ---------------------------------
class Cabinet:
    def __init__(self,clr,dr,clth,hgt,wdt,wgt):
        self.color = clr
        self.door = dr
        self.clothes = clth
        self.height = hgt
        self.width = wdt
        self.weight = wgt

# METHOD OF THE CABINET CLASS
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

# MAIN PROGRAM
# default attributes
Cabinet1 = Cabinet("Brown","Unlocked",5,10,30,80)

# Printed code
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


# THIS IS THE WASHING MACHINE CLASS -------------------------
class WashingMachine:
    def __init__(self,tmr,wtr,clr,ldry,prog):
        self.timer = tmr
        self.water = wtr
        self.color = clr
        self.laundry = ldry 
        self.program = prog #refers to wash program

# METHOD OF WASHING MACHINE CLASS
    def increase_timer(self,n):
        self.timer = self.timer + n

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
# 1 = "gentle"; 2 = "normal"; 3 = "strong"
        self.program = n
    
# MAIN PROGRAM
# default attributes
WashingMachine1 = WashingMachine(20,0,"Blue",5, 2)

# Printed code
print ("7. Washing Machine")
print ("  Color: " + WashingMachine1.color)
print ("  Water (before):", WashingMachine1.water, "gallons")
WashingMachine1.add_water(6) 
print ("  Water (after):", WashingMachine1.water, "gallons")
print ("  No. of Laundry (before):", WashingMachine1.laundry)
WashingMachine1.add_laundry(5)
print ("  No. of Laundry (after):", WashingMachine1.laundry)
print ("  Timer (before):", WashingMachine1.timer, "minutes")
WashingMachine1.increase_timer(5)
print ("  Timer (after):", WashingMachine1.timer, "minutes")
# Below is the if-else-if statement that will return a string instead of the integer indicated in the WashineMachine1.program attribute 
if WashingMachine1.program ==1:
    WashingMachine1.program = "Gentle"
elif WashingMachine1.program == 2:
    WashingMachine1.program = "Normal"
elif WashingMachine1.program == 3:
    WashingMachine1.program = "Strong"
print ("  Wash Program: " + WashingMachine1.program)
print (" ")

# THIS IS THE BED CLASS -------------------------------------
class Bed:
    def __init__(self,clr,wdt,lth,bsht,plw,blkt):
        self.color = clr
        self.width = wdt
        self.length = lth
        self.bedsheet = bsht
        self.pillows = plw
        self.blanket = blkt

# METHOD OF THE BED CLASS
    def give_color(self,n):
        self.color = n

    def give_width(self,n):
        self.width = n

    def give_length(self,n):
        self.length = n

    def change_bedsheet(self,n): #change bedsheet design
        self.bedsheet = n

    def add_pillows(self,n):
        self.pillows = self.pillows + n

    def remove_pillows(self,n):
        self.pillows = self.pillows - n

    def change_blanket(self,n):  #change bedsheet design
        self.blanket = n

# MAIN PROGRAM
# default attributes
myBed = Bed("Gray",500,150,"Black",2,"Pattern")

# Printed cod
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
