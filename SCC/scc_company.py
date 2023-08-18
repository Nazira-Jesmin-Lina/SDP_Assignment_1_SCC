from abc import ABC, abstractmethod
from Enum import *
from car_parts import *

class SCC(ABC):
    def orderCar(self, carType, budgetType, carColor):
        carPartsFactory = self.assembleCarParts(budgetType)
        car = self.createCar(carType, carPartsFactory)
        car.prepareCar(carColor)
        return car

    @abstractmethod
    def createCar(self, carType, carPartsFactory):
        pass

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


