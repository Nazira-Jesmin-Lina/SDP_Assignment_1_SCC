from abc import ABC, abstractmethod
from Car_external_accesories import *
from Car_internal_accesories import *

class Car(ABC):   #abstract method
    def __init__(self):
        self.engine = None
        self.tire = None
        self.ac = None
        self.chassis = None
        self.carColor = None
        self.seat = None
        self.bodyDesign = None
        self.automation = None

    @abstractmethod
    def prepareCar(self, carColor):
        pass

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def getDescription(self):
        pass

class RacingCar(Car):
    def __init__(self, carPartsFactory, companyFactory, automationFactory):
        super().__init__()
        self.carPartsFactory = carPartsFactory
        self.companyFactory = companyFactory
        self.automationFactory = automationFactory

    def prepareCar(self, carColor):
        self.engine = self.carPartsFactory.createEngine()
        self.tire = self.carPartsFactory.createTire()
        self.ac = self.carPartsFactory.createAC()
        self.chesis = self.carPartsFactory.createChesis()
        self.bodyDesign = self.companyFactory.createBodyDesign()
        self.automation = self.automationFactory.createAutomation()
        self.seat = RacingCarSeat()
        self.carColor = carColor

    def cost(self):
        return (
            self.engine.cost()
            + self.tire.cost()
            + self.chesis.cost()
            + self.automation.cost()
            + self.bodyDesign.cost()
            + self.ac.cost()
            + 100
        )

    def getDescription(self):
        return (
            "Racing Car Description \n"
            + "\t" +self.bodyDesign.getName() +"\n"
            + "\t" +self.automation.getName() +"\n"
            + "Internal Components: \n"
            + "\t" +self.engine.getName() +"\n"
            + "\t" +self.tire.getName() +"\n"
            + "\t" +self.chesis.getName() +"\n"
            + "External Components: \n"
            + "\t" +self.ac.getName() +"\n"
            + "\t" +self.seat.getName() +"\n"
            
        )

class PrivateCar(Car):
    def __init__(self, carPartsFactory, companyFactory, automationFactory):
        super().__init__()
        self.carPartsFactory = carPartsFactory
        self.companyFactory = companyFactory
        self.automationFactory = automationFactory

    def prepareCar(self, carColor):
        self.engine = self.carPartsFactory.createEngine()
        self.tire = self.carPartsFactory.createTire()
        self.ac = self.carPartsFactory.createAC()
        self.chesis = self.carPartsFactory.createChesis()
        self.bodyDesign = self.companyFactory.createBodyDesign()
        self.automation = self.automationFactory.createAutomation()
        self.seat = PrivateCarSeat()
        self.carColor = carColor

    def cost(self):
        return (
            self.engine.cost()
            + self.tire.cost()
            + self.chesis.cost()
            + self.automation.cost()
            + self.bodyDesign.cost()
            + self.ac.cost()
            + 50
        )

    def getDescription(self):
        return (
            "Private Car Description \n"
            + "\t" +self.bodyDesign.getName() +"\n"
            + "\t" +self.automation.getName() +"\n"
            + "Internal Components: \n"
            + "\t" +self.engine.getName() +"\n"
            + "\t" +self.tire.getName() +"\n"
            + "\t" +self.chesis.getName() +"\n"
            + "External Components: \n"
            + "\t" +self.ac.getName() +"\n"
            + "\t" +self.seat.getName() +"\n"
            
        )

class SUVCar(Car):
    def __init__(self, carPartsFactory, companyFactory, automationFactory):
        super().__init__()
        self.carPartsFactory = carPartsFactory
        self.companyFactory = companyFactory
        self.automationFactory = automationFactory

    def prepareCar(self, carColor):
        self.engine = self.carPartsFactory.createEngine()
        self.tire = self.carPartsFactory.createTire()
        self.ac = self.carPartsFactory.createAC()
        self.chesis = self.carPartsFactory.createChesis()
        self.bodyDesign = self.companyFactory.createBodyDesign()
        self.automation = self.automationFactory.createAutomation()
        self.seat = SUVCarSeat()
        self.carColor = carColor

    def cost(self):
        return (
            self.engine.cost()
            + self.tire.cost()
            + self.chesis.cost()
            + self.automation.cost()
            + self.bodyDesign.cost()
            + self.ac.cost()
            + 150
        )

    def getDescription(self):
        return (
            "SUV Car Description \n"
            + "\t" +self.bodyDesign.getName() +"\n"
            + "\t" +self.automation.getName() +"\n"
            + "Internal Components: \n"
            + "\t" +self.engine.getName() +"\n"
            + "\t" +self.tire.getName() +"\n"
            + "\t" +self.chesis.getName() +"\n"
            + "External Components: \n"
            + "\t" +self.ac.getName() +"\n"
            + "\t" +self.seat.getName() +"\n"
            
        )

class MilitaryCar(Car):
    def __init__(self, carPartsFactory, companyFactory, automationFactory):
        super().__init__()
        self.carPartsFactory = carPartsFactory
        self.companyFactory = companyFactory
        self.automationFactory = automationFactory

    def prepareCar(self, carColor):
        self.engine = self.carPartsFactory.createEngine()
        self.tire = self.carPartsFactory.createTire()
        self.ac = self.carPartsFactory.createAC()
        self.chesis = self.carPartsFactory.createChesis()
        self.bodyDesign = self.companyFactory.createBodyDesign()
        self.automation = self.automationFactory.createAutomation()
        self.seat = MilitaryCarSeat()
        self.carColor = carColor

    def cost(self):
        return (
            self.engine.cost()
            + self.tire.cost()
            + self.chesis.cost()
            + self.automation.cost()
            + self.bodyDesign.cost()
            + self.ac.cost()
            + 200
        )

    def getDescription(self):
        return (
            "Military Car Description \n"
            + "\t" +self.bodyDesign.getName() +"\n"
            + "\t" +self.automation.getName() +"\n"
            + "Internal Components: \n"
            + "\t" +self.engine.getName() +"\n"
            + "\t" +self.tire.getName() +"\n"
            + "\t" +self.chesis.getName() +"\n"
            + "External Components: \n"
            + "\t" +self.ac.getName() +"\n"
            + "\t" +self.seat.getName() +"\n"
            
        )



