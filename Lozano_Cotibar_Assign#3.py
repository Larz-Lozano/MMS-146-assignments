print ("08/25/2023")
print ("MMS 146 - Assignment #3")
print ("Submitted by: Laryze Lozano and Jeremias Cotibar")
print ("")

#PARENT CLASS 
"""the Device class was added to contain attributes that both
the Smartphone and Laptop class have. We set the lockscreen password
attribute in private since, in the real world, it is a sensitive information"""

class Device: 
    def __init__(self, br, os, batt, vol, blt, pw):
        self.brand = br
        self.os = os 
        self.battery = batt
        self.volume = vol
        self.bluetooth = blt
        self.__lockscreenPass = pw #private

    def give_brand(self):
        print (" Brand:", self.brand)

    def give_os(self):
        print (" Operationg System:", self.os)

    def print_battery(self):
        print (" Battery:", self.battery , "%")

    def increase_volume(self,n):
        self.volume = self.volume + n 
        print (" Volume:", self.volume)

    def connect_bluetooth(self,n):
        self.bluetooth = n
        """Below is the if-else statement that will will return a sring instead of the integer.
        ==1 is equivalent to bluetooth connected; <1 or >1 is equivalent to bluetooth disconnected"""
        if self.bluetooth == 1:
            self.bluetooth = "Connected"
        else:
            self.bluetooth = "Disconnected"
        print (" Bluetooth:", self.bluetooth)

     # Below are the setter and getter method to display the password attribute
    def get_lockscreenPass(self):
        print (" Password:",self.__lockscreenPass)

    def set_lockscreenPass(self,n):
        self.__lockscreenPass = n
        print (" Password:",self.__lockscreenPass)


#CHILD CLASS: SMARTPHONE
"""We added the flashlight and phone number attributes
to the Smartphone class and removed the color and resolution
to decrease the number of attributes and the rest of the attributes
were included under the parent class. The phone number was set in private"""

class Smartphone(Device): 
    def __init__(self, br, os, batt, aud, blt, pw, fl, num):
        super().__init__(br, os, batt, aud, blt, pw) 
        self.flashlight = fl 
        self.__phoneNumber = num #private

    def print_flashlight(self,n):
        self.flashlight = n
        #Below is the if-else statement. ==1 will print "on" while <1 or >1 will print "off"
        if self.flashlight == 1:
            self.flashlight = "On"
        else:
            self.flashlight = "Off"
        print (" Flashlight:", self.flashlight)

    #Below is the getter method for the phone number attribute
    def get_phoneNumber(self):
        print (" Phone Number:", self.__phoneNumber)


#MAIN PROGRAM
# default iphone attributes 
iphone = Smartphone("Apple", "iOS 15", 80, 50, 0, "08124", 0, "0945 430 5310")

print ("Smartphone")
iphone.give_brand()
iphone.give_os()
iphone.print_battery()
iphone.increase_volume(3)
iphone.connect_bluetooth(0)
iphone.print_flashlight(1)
#The codes below will print the private attributes of Smartphone for private attributes/method
"""
iphone.get_lockscreenPass()
iphone.set_lockscreenPass(34964)
iphone.get_phoneNumber()
"""


#CHILD CLASS: Laptop
""" We added the backlit keyboard, touchpad, and IP address attributes to the laptop class.
the IP address is set to private"""

class Laptop(Device): 
    def __init__(self, br, os, batt, vol, blt, pw, backkey, tp, ip):
        super().__init__(br, os, batt, vol, blt, pw)
        self.backlit_keyboard = backkey
        self.touchpad = tp
        self.__ipaddress = ip #private

    def print_backlit_keyboard(self, backkey):
        self.backlit_keyboard = backkey
        #Below is the if-else statement
        if self.backlit_keyboard >= 1:
            print ("  Backlit Keyboard: On")
        else:
            print ("  Backlit Keyboard: Off")
            print (" ")

    def print_touchpad(self, tp):
        self.touchpad = tp
        #Below is the if-else statement
        if self.touchpad >= 1:
            print ("  Touchpad: On")
        else:
            print ("  Touchpad: Off")
            print (" ")

    def set_ipaddress(self,ip):
        self.__ipaddress = ip

    def get_ipaddress(self):
        print (self.__ipaddress)
    
#Main Program
myLaptop = Laptop("Epple","MACOSN",100,10,0,"04321",1,1,"192 168 0 0")

print ("Laptop")
myLaptop.give_brand()
myLaptop.give_os()
myLaptop.print_battery()
myLaptop.increase_volume(5)
myLaptop.connect_bluetooth(1)
myLaptop.print_backlit_keyboard(1)
myLaptop.print_touchpad(1)
#The codes below are to get the private attributes of the laptop class
"""
myLaptop.get_lockscreenPass()
myLaptop.get_ipaddress()
"""



