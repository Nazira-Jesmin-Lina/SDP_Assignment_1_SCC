from abc import ABC,abstractmethod

from car import *
from define_enum import *


class CarService(ABC):
    @abstractmethod
    def execute(self):
        pass

        

class CarWashingService(CarService):
    def execute(self,car,name,cartype):
        payment=0
        if  cartype == CarType.PRIVATE:
            payment= 5
        elif  cartype == CarType.MILITARY:
            payment= 20
        elif  cartype == CarType.RACING:
            payment= 17
        elif  cartype == CarType.SUV:
            payment= 15
        print(f"Washing done for {name}'s {car.getDescription()} \nTotal Payment for washing: {payment}")
        print("_____________________________________________________________________________________")



class CarServicingService(CarService):
    def execute(self,car,name,cartype):
        payment=0
        if  cartype == CarType.PRIVATE:
            payment= 10
        elif  cartype == CarType.MILITARY:
            payment= 30
        elif  cartype == CarType.RACING:
            payment= 17
        elif  cartype == CarType.SUV:
            payment= 15
        print(f"Servicing done for {name}'s {car.getDescription()} \nTotal Payment for washing: {payment}")
        print("_____________________________________________________________________________________")



class OnlineDeliveryService:
    def deliver_car(self,name ,car):
       

        print(f"Delivering {name}'s car.\nCar Description:\n {car.getDescription()} Total cost of the car is:{ car.cost()}")
        print("_____________________________________________________________________________________")


