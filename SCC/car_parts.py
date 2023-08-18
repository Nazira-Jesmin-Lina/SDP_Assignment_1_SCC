from abc import ABC, abstractmethod
from Car_external_accesories import *
from Car_internal_accesories import *

# Abstract Factory Pattern

class CarPartsFactory(ABC):
    @abstractmethod
    def createEngine(self):
        pass
    
    @abstractmethod
    def createTire(self):
        pass
    
    @abstractmethod
    def createAC(self):
        pass
    
    @abstractmethod
    def createChesis(self):
        pass

class LowBudgetCarPartsFactory(CarPartsFactory):
    def createEngine(self):
        return CC1300()
    
    def createTire(self):
        return Snow()
    
    def createAC(self):
        return LowPoweredAC()
    
    def createChesis(self):
        return Tabular()

class MediumLowBudgetCarPartsFactory(CarPartsFactory):
    def createEngine(self):
        return CC1700()
    
    def createTire(self):
        return Spare()
    
    def createAC(self):
        return LowPoweredAC()
    
    def createChesis(self):
        return Backbone()

class MediumHighBudgetCarPartsFactory(CarPartsFactory):
    def createEngine(self):
        return CC1800()
    
    def createTire(self):
        return Whitewall()
    
    def createAC(self):
        return HighPoweredAC()
    
    def createChesis(self):
        return LadderFrame()

class HighBudgetCarPartsFactory(CarPartsFactory):
    def createEngine(self):
        return CC2100()
    
    def createTire(self):
        return Slick()
    
    def createAC(self):
        return HighPoweredAC()
    
    def createChesis(self):
        return LadderFrame()

