from abc import ABC,abstractmethod

from car import *


class CarService(ABC):
    def __init__(self, car):
        self.car = car
    @abstractmethod
    def execute(self):
        pass

        

class CarWashingService(CarService):
    def execute(self):
        payment=0
        if  self.car == "PRIVATE":
            payment= 5
        elif  self.car == "MILITARY":
            payment= 17
        elif  self.car == "SUV":
            payment= 10
        elif  self.car == "RACING":
            payment= 18
        print(f"Washing {self.car} car.Total Payment: {payment}")


class CarServicingService(CarService):
    def execute(self):
        payment=0
        if self.car == "PRIVATE":
            payment = 11
        elif  self.car == "MILITARY":
            payment = 20
        elif  self.car == "SUV":
            payment = 15
        elif  self.car == "RACING":
            payment = 18
        print(f"Servicing {self.car} car.Total Payment: {payment}")


class OnlineDeliveryService:
    def deliver_car(self, car):
        
        print(f"Delivering {car.body_design} car to the client.\n details:\n {car.getDescription}")
