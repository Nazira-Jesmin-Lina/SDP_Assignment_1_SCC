from car_decorator import *

# Decorator Pattern

class ThickRainShield(CarDecorator):
    def __init__(self, car):
        self.car = car

    def cost(self):
        return 2 + self.car.cost()

    def getDescription(self):
        return self.car.getDescription() + "customized Decorator: ThickRainShield \n"

class ThinRainShield(CarDecorator):
    def __init__(self, car):
        self.car = car

    def cost(self):
        return 5 + self.car.cost()

    def getDescription(self):
        return self.car.getDescription() + "customized Decorator: ThinRainShield \n"

class CurvedRainShield(CarDecorator):
    def __init__(self, car):
        self.car = car

    def cost(self):
        return 10 + self.car.cost()

    def getDescription(self):
        return self.car.getDescription() + "customized Decorator: CurvedRainShield \n"



class TightBumper(CarDecorator):
    def __init__(self, car):
        self.car = car

    def prepareCar(self, carColor):
        self.car.prepareCar(carColor)

    def cost(self):
        return 10 + self.car.cost()

    def getDescription(self):
        return self.car.getDescription() + "customized Decorator: TightBumper \n"

class LooseBumper(CarDecorator):
    def __init__(self, car):
        self.car = car

    def prepareCar(self, carColor):
        self.car.prepareCar(carColor)

    def cost(self):
        return 5 + self.car.cost()

    def getDescription(self):
        return self.car.getDescription() + "customized Decorator: LooseBumper \n"


class MobileBasedControlSystem(CarDecorator):
    def __init__(self, car):
        self.car = car

    def cost(self):
        return 20 + self.car.cost()

    def getDescription(self):
        return self.car.getDescription() + "customized Decorator: MobileBasedGateControllingSystem \n"

class RemoteBasedControlSystem(CarDecorator):
    def __init__(self, car):
        self.car = car

    def cost(self):
        return 10 + self.car.cost()

    def getDescription(self):
        return self.car.getDescription() + "customized Decorator: RemoteBasedGateControllingSystem \n"


class OpenRoofSystem(CarDecorator):
    def __init__(self, car):
        self.car = car

    def cost(self):
        return 20 + self.car.cost()

    def getDescription(self):
        return self.car.getDescription() + "customized Decorator: OpenRoofSystem \n"
