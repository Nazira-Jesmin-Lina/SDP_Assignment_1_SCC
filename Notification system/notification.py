class NotificationSystem:
    _unique_instance = None

    def __init__(self):
        self.subscriber_set = set()

    @classmethod
    def get_instance(cls):
        if cls._unique_instance is None:
            cls._unique_instance = cls()
        return cls._unique_instance

    def register_subscriber(self, subscriber):
        self.subscriber_set.add(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscriber_set.remove(subscriber)

    def notify_subscribers_for_price_change(self):
        for subscriber in self.subscriber_set:
            subscriber.update("Some cars price has been changed. Please visit our website to see the updates...\n\n")

    def notify_subscriber_for_car_feature_change(self):
        for subscriber in self.subscriber_set:
            subscriber.update("Some cars basic features have been changed. Please visit our website to see the updates...\n\n")

    def price_change(self):
        self.notify_subscribers_for_price_change()

    def basic_features_change(self):
        self.notify_subscriber_for_car_feature_change()