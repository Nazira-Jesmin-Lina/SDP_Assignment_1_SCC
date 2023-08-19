from abc import ABC, abstractmethod
from define_enum import *
from car_parts import *
from web_backend import *


class SCC(ABC):
    def orderCar(self, carType, budgetType, carColor):
        carPartsFactory = self.assembleCarParts(budgetType)
        car = self.createCar(carType, carPartsFactory)
        car.prepareCar(carColor)
        return car
    
    def serviceCar(self,name,serviceType, carType , budgetType, carColor):
        web=WebBackend()
        car=SCC.orderCar(self, carType, budgetType, carColor)
        web.request_service(name,serviceType,carType,car)


    def onlineOrder(self, name,carType, budgetType, carColor):
        car= SCC.orderCar(self, carType, budgetType, carColor)
        web=WebBackend()
        web.request_delivery(name,car)

        
        

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
