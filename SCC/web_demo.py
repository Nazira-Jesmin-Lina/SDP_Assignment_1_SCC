from car import *
from scc_company import *
from car_type import *
from define_enum import *



a= FordAmerica()
a.serviceCar("Rizvee Sir","Wash",CarType.PRIVATE, BudgetType.LOW, CarColor.BLACK)
a.onlineOrder( "Mr.X",CarType.PRIVATE, BudgetType.LOW, CarColor.BLACK)
b=ToyotaAmerica()
b.serviceCar("Dipto","Service",CarType.PRIVATE, BudgetType.LOW, CarColor.BLACK)
b.onlineOrder( "Dipto",CarType.SUV, BudgetType.LOW, CarColor.BLACK)
