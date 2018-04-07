# class Bike(object):
#     def sayHello(self):
#         print "Hello"

# bike1 = Bike()
# bike1.sayHello()



class Bike(object):
    def __init__(self, price, maxspeed, miles):
        self.price = price
        self.maxspeed = maxspeed
        self.miles = miles
    def sayHello(self):
        print "Hello"
    def displayinfo(self):
        print self.price, self.maxspeed, self.miles


bike1 = Bike(200, "25mph", 2500)
bike2 = Bike(500, "30mph", 100)
bike3 = Bike(1200, "55mph", 500)

print bike1.price
bike1.sayHello()
bike1.displayinfo()