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


#This is the Laptop Class
class Laptop:
    def __init__(self,brand,batt,color,bright,backkey,weight,width,os):
        self.brand = brand
        self.battery = batt
        self.color = color
        self.brightness = bright
        self.backlit_keyboard = backkey
        self.weight = weight
        self.width = width
        self.os = os

#This is the methods for the Laptop Class
    def give_brand(self,brand):
        self.brand = brand

    def give_battery(self,batt):
        self.battery = batt

    def increase_battery(self,batt):
        self.battery = self.battery + 1

    def decrease_battery(self,batt):
        self.battery = self.battery - 1

    def give_color(self,color):
        self.color = color

    def increase_brightness(self,bright):
        self.brightness = self.brightness + 1

    def decrease_brightness(self,bright):
        self.brightness = self.brightness - 1

    def on_backlit_keyboard(self,backkey):
        self.backlit_keyboard = backlit_keyboard

    def off_backlit_keyboard(self,backkey):
        self.backlit_keyboard = backlit_keyboard

    def update_os(self,os):
        self.os = os

#Main Program
Laptop1 = Laptop("apple",100,"white",10,100,200,300,"macosx")


print (Laptop1.brand)
print (Laptop1.battery)
print (Laptop1.color)
print (Laptop1.os)
print ("before increase brightness: ", Laptop1.brightness)
Laptop1.increase_brightness("0")
print ("after increase brightness: ", Laptop1.brightness)


#This is the Book Class
class Book:
    def __init__(self,title,author,height,weight,width,page):
        self.title = title
        self.author = author
        self.height = height
        self.weight = weight
        self.width = width
        self.page = page

#This is the methods for the Book Class
    def give_title(self,title):
        self.title = title

    def name_author(self,author):
        self.author = author

    def give_height(self,height):
        self.height = height

    def give_weight(self,weight):
        self.weight = weight

    def give_width(self,width):
        self.width = width

    def next_page(self,page):
        self.page = self.page + 1

    def previous_page(self,page):
        self.page = self.page - 1

    def bookmark_page(self,page):
        self.page = page

    def give_page(self,page):
        self.page = page

#Main Program
Book1 = Book("harrypotter","jkrowling",7,101,5,300)


print (Book1.title)
print (Book1.author)
print (Book1.height)
print (Book1.page)
print ("before next page: ", Book1.page)
Book1.next_page("0")
print ("after next page: ", Book1.page)
    

#This is the Cabinet Class
class Cabinet:
    def __init__(self,color,door,clothes,height,width,weight):
        self.color = color
        self.door = door
        self.clothes = clothes
        self.height = height
        self.width = width
        self.weight = weight

#This is the methods for the Cabinet Class
    def give_color(self,color):
        self.color = color

    def unlock_door(self,door):
        self.door = door

    def lock_door(self,door):
        self.door = door

    def give_height(self,height):
        self.height = height

    def give_width(self,width):
        self.width = width

    def give_weight(self,weight):
        self.weight = weight

    def add_clothes(self,clothes):
        self.clothes = self.clothes + 1

    def remove_clothes(self,clothes):
        self.clothes = self.clothes - 1

#Main Program
Cabinet1 = Cabinet("brown","normal",1,30,20,80)

print (Cabinet1.color)
print (Cabinet1.door)
print (Cabinet1.height)
print (Cabinet1.weight)
print ("before lock door: ", Cabinet1.door)
Cabinet1.lock_door("locked")
print ("after lock door: ", Cabinet1.door)    


#This is the Washing Machine Class
class WashingMachine:
    def __init__(self,timer,water,color,laundry,program):
        self.timer = timer
        self.water = water
        self.color = color
        self.laundry = laundry
        self.program = program

#This is the methods for the Washing Machine Class
    def increase_timer(self,timer):
        self.timer = self.timer + 1

    def add_water(self,water):
        self.water = self.water + 1

    def drain_water(self,water):
        self.water = self.water - 1

    def give_color(self,color):
        self.color = color

    def add_laundry(self,laundry):
        self.laundry = self.laundry + 1

    def remove_laundry(self,laundry):
        self.laundry = self.laundry - 1

    def gentle_program(self,program):
        self.program = program

    def normal_program(self,program):
        self.program = program

    def strong_program(self,program):
        self.program = program
    
#Main Program
WashingMachine1 = WashingMachine(60,100,"blue","laundry","normal")


print (WashingMachine1.program)
print (WashingMachine1.color)
print ("before add water: ", WashingMachine1.water)
WashingMachine1.add_water(0)
print ("after add water: ", WashingMachine1.water)
print ("before normal program: ", WashingMachine1.program)
WashingMachine1.normal_program("strong")
print ("after normal program: ", WashingMachine1.program)


#This is the Bed Class
class Bed:
    def __init__(self,color,width,length,bedsheet,pillows,blanket):
        self.color = color
        self.width = width
        self.length = length
        self.bedsheet = bedsheet
        self.pillows = pillows
        self.blanket = blanket

#This is the methods for the Bed Class
    def give_color(self,color):
        self.color = color

    def give_width(self,width):
        self.width = 500

    def give_length(self,length):
        self.length = 150

    def change_bedsheet(self,bedsheet):
        self.bedsheet = bedsheet

    def add_pillows(self,pillows):
        self.pillows = self.pillows + 1

    def remove_pillows(self,pillows):
        self.pillows = self.pillows - 1

    def change_blanket(self,blanket):
        self.blanket = blanket

#Main Program
Bed1 = Bed("gray",500,150,"black",2,"pattern")


print (Bed1.color)
print (Bed1.width)
print (Bed1.bedsheet)
print (Bed1.blanket)
print ("blanket before: ", Bed1.blanket)
Bed1.change_blanket("stripes")
print ("blanket after: ", Bed1.blanket)