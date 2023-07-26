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
        self.title = harrypotter

    def name_author(self,author):
        self.author = jkrowling

    def give_height(self,height):
        self.height = 7

    def give_weight(self,weight):
        self.weight = 101

    def give_width(self,width):
        self.width = 5

    def next_page(self,page):
        self.page = self.page + 1

    def previous_page(self,page):
        self.page = self.page - 1

    def bookmark_page(self,page):
        self.page = bookmarked

    def give_page(self,page):
        self.page = 300

#Main Program
Book1 = Book("harrypotter","jkrowling",7,101,5,300)


print (Book1.title)
print (Book1.author)
print (Book1.height)
print (Book1.page)
    

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
        self.color = brown

    def unlock_door(self,door):
        self.door = unlocked

    def lock_door(self,door):
        self.door = locked

    def give_height(self,height):
        self.height = 30

    def give_width(self,width):
        self.width = 20

    def give_weight(self,weight):
        self.weight = 80

    def add_clothes(self,clothes):
        self.clothes = self.clothes + 1

    def remove_clothes(self,clothes):
        self.clothes = self.clothes - 1

#Main Program
Cabinet1 = Cabinet("brown","round",1,30,20,80)

print (Cabinet1.color)
print (Cabinet1.door)
print (Cabinet1.height)
print (Cabinet1.weight)    



#This is the Washing Machine Class
class Washing Machine

#This is the Bed Class
class Bed

