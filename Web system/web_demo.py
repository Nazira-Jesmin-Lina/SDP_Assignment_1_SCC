from web_backend import WebBackend


web=WebBackend()
web.request_service("Wash","SUV")
web.request_service("Service","MILITARY")

web.request_service("Wash","PRIVATE")
web.request_service("Service","SUV")
web.request_service("Wash","RACING")
web.request_service("Service","RACING")