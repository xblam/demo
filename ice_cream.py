from restaurant import Restaurant, User

class IceCream(Restaurant):
    def __init__(self, name): 
        super().__init__(name)

    def printName(self):
          # prints the name of the ice cream truck
        print(self.name)

# i1 = IceCream('bens ice cream')
# i1.printName()

class Admin(User):
    def __init__(self, fname, lname, numberServed = 0):
        super().__init__(fname, lname, numberServed = 0)
        self.priviledges = ['can ban people', 'can add people', 'can remove people']
    
    def listPriviledges(self):
          # list the priviledges that the admin has
        print(self.priviledges)

# a1 = Admin('benisteno', 'lam')
# print(a1.firstName)
# a1.listPriviledges()
class Battery():
    def __init__(self):
        self.size = 60
    def upgradeBatttery(self):
        # it upgrades the batter (if nessecary)
        if self.size == 60:
            self.size = 80

class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def Beep(self):
          # honk the horn
        print('get tf outta the way')

class electricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.size = Battery()
    def getRange(self, batsize):
           # return the range of the car
        return(f'{batsize * 4} miles')
    def batSize(self):
          # list the bat size
        print(self.size.size)


