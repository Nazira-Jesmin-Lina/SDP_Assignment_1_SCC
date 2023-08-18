from abc import ABC,abstractmethod

# Abstract Factory Pattern

class Chesis(ABC):
    @abstractmethod
    def cost(self):
        pass
    @abstractmethod
    def getName(self):
        pass

class Tabular(Chesis):
    def cost(self):
        return 5

    def getName(self):
        return "Chesis : Tabular "

class Backbone(Chesis):
    def cost(self):
        return 10

    def getName(self):
        return "Chesis : Backbone"

class LadderFrame(Chesis):
    def cost(self):
        return 15

    def getName(self):
        return "Chesis : LadderFrame"




class Engine(ABC):
    @abstractmethod
    def getName(self):
        pass
    @abstractmethod
    def cost(self):
        pass

class CC1300(Engine):
    def getName(self):
        return "Engine : 1300CC "

    def cost(self):
        return 10

class CC1700(Engine):
    def getName(self):
        return "Engine : 1700CC "

    def cost(self):
        return 20

class CC1800(Engine):
    def getName(self):
        return "Engine : 1800CC "

    def cost(self):
        return 30

class CC2100(Engine):
    def getName(self):
        return "Engine : 2100CC "

    def cost(self):
        return 40






class Tire(ABC):
    @abstractmethod
    def getName(self):
        pass
    
    @abstractmethod
    def cost(self):
        pass

class Snow(Tire):
    def getName(self):
        return "Tire type : Snow"

    def cost(self):
        return 1

class Spare(Tire):
    def getName(self):
        return "Tire type : Spare"

    def cost(self):
        return 2

class Whitewall(Tire):
    def getName(self):
        return "Tire type : Whitewall"

    def cost(self):
        return 3

class Slick(Tire):
    def getName(self):
        return "Tire type : Slick"

    def cost(self):
        return 4





