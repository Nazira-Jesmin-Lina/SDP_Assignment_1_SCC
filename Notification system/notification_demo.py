from notification import *
from subscriber import *

def main():
    notification_system = NotificationSystem.get_instance()

    subscriber1 = SubscriberClient("Batman")
    subscriber2 = SubscriberClient("Ironman")
    subscriber3 = SubscriberClient("Spiderman")

    subscriber1.request_for_subscription()
    subscriber2.request_for_subscription()
    subscriber3.request_for_subscription()

    notification_system.price_change()
   
    subscriber2.request_for_subscription_removal()
   
    notification_system.basic_features_change()
   


if __name__ == "__main__":
    main()