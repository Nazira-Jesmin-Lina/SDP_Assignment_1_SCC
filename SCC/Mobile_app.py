from car_type import *
from define_enum import *


class MobileApp:

    def __init__(self, objct, name, serviceType, carType, budgetType, carColor):
        print("Welcome to SCC's Mobile app")
        if serviceType != "Wash" and serviceType != "Service":
            objct.onlineOrder(name, carType, budgetType, carColor)
        else:
            objct.serviceCar(name, serviceType, carType, budgetType, carColor)
