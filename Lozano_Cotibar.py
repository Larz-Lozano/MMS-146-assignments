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

#This is the method for the Laptop Class
    def give_brand(self,brand):
        self.brand = apple

    def give_battery(self,batt):
        self.battery = 100

    def increase_battery(self,batt):
        self.battery = self.battery + 1

    def decrease_battery(self,batt):
        self.battery = self.battery - 1

    def give_color(self,color):
        self.color = white

    def increase_brightness(self,bright):
        self.brightness = self.brightness + 1

    def decrease_brightness(self,bright):
        self.brightness = self.brightness - 1

    def on_backlit_keyboard(self,backkey):
        self.backlit_keyboard = on

    def off_backlit_keyboard(self,backkey):
        self.backlit_keyboard = off

    def update_os(self,os):
        self.os = update

#Main Program
Laptop1 = Laptop("apple",100,"white",10,100,200,300,"macosx")


print (Laptop1.brand)
print (Laptop1.battery)
print (Laptop1.color)
print (Laptop1.os)

#This is the Book Class
class Book

#This is the Cabinet Class
class Cabinet

#This is the Washing Machine Class
class Washing Machine

#This is the Bed Class
class Bed