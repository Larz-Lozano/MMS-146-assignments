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
    def give_brand(self):
        self.brand = "Semsung"
    def give_color(self):
        self.color = "blue"
# change the number and/or change the sign to minus
    def increase_battery(self):
        self.battery = self.battery + 3
# For simpler writing, >=1 is equal to "No" and <1 is equal to "Yes"
    def mute_audio(self):
        self.audio = 1
        

# MAIN PROGRAM
# default Smartphone attributes
mySmartphone = Smartphone("Semsung", "red", 50, 0, "1920 x 1080", "connect")

# Printed code
print ("My Smartphone")
print ("  Brand: " + mySmartphone.brand)
mySmartphone.give_color()
print ("  Color: " + mySmartphone.color)
print ("  Power: " + mySmartphone.color)
# Below is the if-else statement that will return a string instead of the integer indicated in the mute_audio method
mySmartphone.mute_audio()
if mySmartphone.audio < 1:
    print ("  Mute: Yes")
else:
    print ("  Mute: No")
