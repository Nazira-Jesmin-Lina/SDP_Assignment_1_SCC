from abc import ABC, abstractmethod

#factory method pattern is used
#contains all automation classes


class Automation(ABC):
    @abstractmethod
    def getName(self):
        pass
    
    @abstractmethod
    def cost(self):
        pass

class AsiaAutomation(Automation):
    def getName(self):
        return "Automated by : Asia"
    
    def cost(self):
        return 10

class AmericaAutomation(Automation):
    def getName(self):
        return "Automated by : America"
    
    def cost(self):
        return 5
    



