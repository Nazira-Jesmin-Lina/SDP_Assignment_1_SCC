from web_service import *
from define_enum import *
from car import *

class WebBackend():
    def request_service(self, name,service_type,carType, car):
        if service_type == "Wash":
            car_wash_service = CarWashingService()
            car_wash_service.execute(car,name,carType)
        elif service_type == "Service":
            car_service_service = CarServicingService()
            car_service_service.execute(car,name,carType)

    def request_delivery(self,name, car):
        delivery_service = OnlineDeliveryService()
        delivery_service.deliver_car(name,car)


    