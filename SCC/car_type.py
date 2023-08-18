from scc_company import *
from car import *
from car_factory import *
from ai_sytem import *
from car_parts import *
from define_enum import *

# Abstract Factory Pattern

class FerrariAmerica(SCC):
    def createCar(self, carType, carPartsFactory):
        if carType == CarType.RACING:
            return RacingCar(carPartsFactory, FerrariCompanyFactory(), AmericaAutomationFactory())
        elif carType == CarType.PRIVATE:
            return PrivateCar(carPartsFactory, FerrariCompanyFactory(), AmericaAutomationFactory())
        elif carType == CarType.SUV:
            return SUVCar(carPartsFactory, FerrariCompanyFactory(), AmericaAutomationFactory())
        elif carType == CarType.MILITARY:
            return MilitaryCar(carPartsFactory, FerrariCompanyFactory(), AmericaAutomationFactory())
        else:
            return None


class FerrariAsia(SCC):
    def createCar(self, carType, carPartsFactory):
        if carType == CarType.RACING:
            return RacingCar(carPartsFactory, FerrariCompanyFactory(), AsiaAutomationFactory())
        elif carType == CarType.PRIVATE:
            return PrivateCar(carPartsFactory, FerrariCompanyFactory(), AsiaAutomationFactory())
        elif carType == CarType.SUV:
            return SUVCar(carPartsFactory, FerrariCompanyFactory(), AsiaAutomationFactory())
        elif carType == CarType.MILITARY:
            return MilitaryCar(carPartsFactory, FerrariCompanyFactory(), AsiaAutomationFactory())
        else:
            return None
        

class FordAmerica(SCC):
    def createCar(self, carType, carPartsFactory):
        if carType == CarType.RACING:
            return RacingCar(carPartsFactory, FordsCompanyFactory(), AmericaAutomationFactory())
        elif carType == CarType.PRIVATE:
            return PrivateCar(carPartsFactory, FordsCompanyFactory(), AmericaAutomationFactory())
        elif carType == CarType.SUV:
            return SUVCar(carPartsFactory, FordsCompanyFactory(), AmericaAutomationFactory())
        elif carType == CarType.MILITARY:
            return MilitaryCar(carPartsFactory, FordsCompanyFactory(), AmericaAutomationFactory())
        else:
            return None


class FordAsia(SCC):
    def createCar(self, carType, carPartsFactory):
        if carType == CarType.RACING:
            return RacingCar(carPartsFactory, FordsCompanyFactory(), AsiaAutomationFactory())
        elif carType == CarType.PRIVATE:
            return PrivateCar(carPartsFactory, FordsCompanyFactory(), AsiaAutomationFactory())
        elif carType == CarType.SUV:
            return SUVCar(carPartsFactory, FordsCompanyFactory(), AsiaAutomationFactory())
        elif carType == CarType.MILITARY:
            return MilitaryCar(carPartsFactory, FordsCompanyFactory(), AsiaAutomationFactory())
        else:
            return None

    def assembleCarParts(self, budgetType):
        if budgetType == BudgetType.LOW:
            return LowBudgetCarPartsFactory()
        elif budgetType == BudgetType.MEDIUM_LOW:
            return MediumLowBudgetCarPartsFactory()
        elif budgetType == BudgetType.MEDIUM_HIGH:
            return MediumHighBudgetCarPartsFactory()
        elif budgetType == BudgetType.HIGH:
            return HighBudgetCarPartsFactory()
        else:
            return None


class ToyotaAmerica(SCC):
    def createCar(self, carType, carPartsFactory):
        if carType == CarType.RACING:
            return RacingCar(carPartsFactory, ToyotaCompanyFactory(), AmericaAutomationFactory())
        elif carType == CarType.PRIVATE:
            return PrivateCar(carPartsFactory, ToyotaCompanyFactory(), AmericaAutomationFactory())
        elif carType == CarType.SUV:
            return SUVCar(carPartsFactory, ToyotaCompanyFactory(), AmericaAutomationFactory())
        elif carType == CarType.MILITARY:
            return MilitaryCar(carPartsFactory, ToyotaCompanyFactory(), AmericaAutomationFactory())
        else:
            return None

class ToyotaAsia(SCC):
    def createCar(self, carType, carPartsFactory):
        if carType == CarType.RACING:
            return RacingCar(carPartsFactory, ToyotaCompanyFactory(), AsiaAutomationFactory())
        elif carType == CarType.PRIVATE:
            return PrivateCar(carPartsFactory, ToyotaCompanyFactory(), AsiaAutomationFactory())
        elif carType == CarType.SUV:
            return SUVCar(carPartsFactory, ToyotaCompanyFactory(), AsiaAutomationFactory())
        elif carType == CarType.MILITARY:
            return MilitaryCar(carPartsFactory, ToyotaCompanyFactory(), AsiaAutomationFactory())
        else:
            return None



class ChevroletAmerica(SCC):
    def createCar(self, carType, carPartsFactory):
        if carType == CarType.RACING:
            return RacingCar(carPartsFactory, ChevroletCompanyFactory(), AmericaAutomationFactory())
        elif carType == CarType.PRIVATE:
            return PrivateCar(carPartsFactory, ChevroletCompanyFactory(), AmericaAutomationFactory())
        elif carType == CarType.SUV:
            return SUVCar(carPartsFactory, ChevroletCompanyFactory(), AmericaAutomationFactory())
        elif carType == CarType.MILITARY:
            return MilitaryCar(carPartsFactory, ChevroletCompanyFactory(), AmericaAutomationFactory())
        else:
            return None


class ChevroletAsia(SCC):
    def createCar(self, carType, carPartsFactory):
        if carType == CarType.RACING:
            return RacingCar(carPartsFactory, ChevroletCompanyFactory(), AsiaAutomationFactory())
        elif carType == CarType.PRIVATE:
            return PrivateCar(carPartsFactory, ChevroletCompanyFactory(), AsiaAutomationFactory())
        elif carType == CarType.SUV:
            return SUVCar(carPartsFactory, ChevroletCompanyFactory(), AsiaAutomationFactory())
        elif carType == CarType.MILITARY:
            return MilitaryCar(carPartsFactory, ChevroletCompanyFactory(), AsiaAutomationFactory())
        else:
            return None

class BMWAmerica(SCC):
    def createCar(self, carType, carPartsFactory):
        if carType == CarType.RACING:
            return RacingCar(carPartsFactory, BMWCompanyFactory(), AmericaAutomationFactory())
        elif carType == CarType.PRIVATE:
            return PrivateCar(carPartsFactory, BMWCompanyFactory(), AmericaAutomationFactory())
        elif carType == CarType.SUV:
            return SUVCar(carPartsFactory, BMWCompanyFactory(), AmericaAutomationFactory())
        elif carType == CarType.MILITARY:
            return MilitaryCar(carPartsFactory, BMWCompanyFactory(), AmericaAutomationFactory())
        else:
            return None


class BMWAsia(SCC):
    def createCar(self, carType, carPartsFactory):
        if carType == CarType.RACING:
            return RacingCar(carPartsFactory, BMWCompanyFactory(), AsiaAutomationFactory())
        elif carType == CarType.PRIVATE:
            return PrivateCar(carPartsFactory, BMWCompanyFactory(), AsiaAutomationFactory())
        elif carType == CarType.SUV:
            return SUVCar(carPartsFactory, BMWCompanyFactory(), AsiaAutomationFactory())
        elif carType == CarType.MILITARY:
            return MilitaryCar(carPartsFactory, BMWCompanyFactory(), AsiaAutomationFactory())
        else:
            return None



