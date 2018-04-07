class Car(object):
    def __init__(self, price, speed, fuel, milage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage
        self.display_all()
    def display_all(self):
        print self.price, self.speed, self.fuel, self.milage

car1 = Car(5000, "60mph", "gas", 50000)
car2 = Car(4000, "60mph", "gas", 50000)
car3 = Car(20000, "80mph", "diesel", 50000)
car4 = Car(10000, "70mph", "diesel", 50000)


        
