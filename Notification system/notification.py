from abc import ABC, abstractmethod
# Observer Pattern 
class NotificationSubject(ABC):
    @abstractmethod
    def register_subscriber(self, subscriber):
        pass

    @abstractmethod
    def remove_subscriber(self, subscriber):
        pass

    @abstractmethod
    def notify_subscribers_for_price_change(self):
        pass

    @abstractmethod
    def notify_subscriber_for_car_feature_change(self):
        pass

class NotificationSystem(NotificationSubject):
    def __init__(self):
        self.subscriber_set = set()
        self.unique_instance = None

    @staticmethod
    def get_instance():
        if NotificationSystem.unique_instance is None:
            NotificationSystem.unique_instance = NotificationSystem()
        return NotificationSystem.unique_instance

    def register_subscriber(self, subscriber):
        self.subscriber_set.add(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscriber_set.remove(subscriber)

    def notify_subscribers_for_price_change(self):
        for subscriber in self.subscriber_set:
            subscriber.update("Some cars price has been changed. Please visit our website to see the changes...")

    def notify_subscriber_for_car_feature_change(self):
        for subscriber in self.subscriber_set:
            subscriber.update("Some cars basic features has been changed. Please visit our website to see the changes...")

    def price_change(self):
        self.notify_subscribers_for_price_change()

    def basic_features_change(self):
        self.notify_subscriber_for_car_feature_change()

class Subscriber:
    def update(self, message):
        print("Received update:", message)
