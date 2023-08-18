class CarService:
    def __init__(self, car):
        self.car = car

    def execute(self):
        pass


class CarWashingService(CarService):
    def execute(self):
        print(f"Washing {self.car.body_design} car.")


class CarServicingService(CarService):
    def execute(self):
        print(f"Servicing {self.car.body_design} car.")


class OnlineDeliveryService:
    def deliver_car(self, car):
        print(f"Delivering {car.body_design} car to the client.")
