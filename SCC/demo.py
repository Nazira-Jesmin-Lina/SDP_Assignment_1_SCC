from car import *
from car_type import *
from car_customization import *
from car_decorator import *
from car_factory import *
from Car_external_accesories import *
from car_parts import *
from ai_sytem import *
from scc_company import *



def main():
    scc = FordAmerica()
    car = scc.orderCar(CarType.PRIVATE, BudgetType.LOW, CarColor.BLACK)
    print("_____________________________________________________________________________________")
    print(car.getDescription())
    print("Total cost of the car is:", car.cost())

    car = ThickRainShield(car)
    print("_____________________________________________________________________________________")
    print(car.getDescription())
    print("Total cost of the car is:", car.cost())

    car = TightBumper(car)
    print("_____________________________________________________________________________________")
    print(car.getDescription())
    print("Total cost of the car is:", car.cost())

    car = MobileBasedControlSystem(car)
    print("_____________________________________________________________________________________")
    print(car.getDescription())
    print("Total cost of the car is:", car.cost())

    car = OpenRoofSystem(car)
    print("_____________________________________________________________________________________")
    print(car.getDescription())
    print("Total cost of the car is:", car.cost())

if __name__ == "__main__":
    main()
