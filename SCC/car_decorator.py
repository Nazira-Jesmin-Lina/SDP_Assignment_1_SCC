from car import *

#  Decorator Pattern

class CarDecorator(Car):
    def prepareCar(self, carColor):
        try:
            raise Exception()
        except Exception as e:
            print("Preparation of car must be before decoration")


