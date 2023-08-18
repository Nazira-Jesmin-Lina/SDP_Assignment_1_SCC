from car_service import *
from define_enum import *
from car import *

class WebBackend():
    def request_service(self, service_type, car):
        if service_type == "Wash":
            car_wash_service = CarWashingService(car)
            car_wash_service.execute()
        elif service_type == "Service":
            car_service_service = CarServicingService(car)
            car_service_service.execute()

    def request_delivery(self, car):
        delivery_service = OnlineDeliveryService()
        delivery_service.deliver_car(car)


    