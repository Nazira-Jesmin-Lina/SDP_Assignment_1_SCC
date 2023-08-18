from notification import *

# observer pattern

class Subscriber:
    def update(self, message):
        pass

    def request_for_subscription(self):
        pass

    def request_for_subscription_removal(self):
        pass

class SubscriberClient(Subscriber):
    def __init__(self, name):
        self.name = name
        self.notification_system = NotificationSystem.get_instance()

    def update(self, message):
        print(f"Hello {self.name}, we have an update for you")
        print(message)

    def request_for_subscription(self):
        self.notification_system.register_subscriber(self)

    def request_for_subscription_removal(self):
        self.notification_system.remove_subscriber(self)
