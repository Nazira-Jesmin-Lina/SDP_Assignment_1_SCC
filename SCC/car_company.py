from abc import ABC,abstractmethod
# Abstract Factory Pattern

class BodyDesign(ABC):
    @abstractmethod
    def getName(self):
        pass
    
    @abstractmethod
    def cost(self):
        pass

class Fords(BodyDesign):
    def getName(self):
        return "Company Name : Fords "

    def cost(self):
        return 10

class Ferrari(BodyDesign):
    def getName(self):
        return "Company Name : Ferrari"

    def cost(self):
        return 30

class Toyota(BodyDesign):
    def getName(self):
        return "Company Name : Toyota"

    def cost(self):
        return 20

class BMW(BodyDesign):
    def getName(self):
        return "Company Name : BMW"

    def cost(self):
        return 50

class Chevrolet(BodyDesign):
    def getName(self):
        return "Company Name : Chevrolet"

    def cost(self):
        return 40
