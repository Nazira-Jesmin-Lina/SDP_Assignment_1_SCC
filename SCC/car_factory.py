from abc import ABC, abstractmethod
from Car_external_accesories import *
from ai_sytem import *
from car_company import *

# Abstract Factory Pattern

class CompanyFactory(ABC):
    @abstractmethod
    def createBodyDesign(self):
        pass

class FordsCompanyFactory(CompanyFactory):
    def createBodyDesign(self):
        return Fords()

class FerrariCompanyFactory(CompanyFactory):
    def createBodyDesign(self):
        return Ferrari()

class ToyotaCompanyFactory(CompanyFactory):
    def createBodyDesign(self):
        return Toyota()

class BMWCompanyFactory(CompanyFactory):
    def createBodyDesign(self):
        return BMW()

class ChevroletCompanyFactory(CompanyFactory):
    def createBodyDesign(self):
        return Chevrolet()







#automation factory

class AutomationFactory(ABC):
    @abstractmethod
    def createAutomation(self):
        pass

class AsiaAutomationFactory(AutomationFactory):
    def createAutomation(self):
        return AsiaAutomation()

class AmericaAutomationFactory(AutomationFactory):
    def createAutomation(self):
        return AmericaAutomation()


