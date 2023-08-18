from abc import ABC,abstractmethod

# Abstract Factory Pattern along with the Factory Method Pattern.

class Seat(ABC):
    @abstractmethod
    def getName(self):
        pass
    
    @abstractmethod
    def totalSeats(self):
        pass

class RacingCarSeat(Seat):
    def getName(self):
        return "Total Seats : " + str(self.totalSeats()) 

    def totalSeats(self):
        return 1

class PrivateCarSeat(Seat):
    def getName(self):
        return "Total Seats : " + str(self.totalSeats()) 

    def totalSeats(self):
        return 5

class SUVCarSeat(Seat):
    def getName(self):
        return "Total Seats : " + str(self.totalSeats()) 

    def totalSeats(self):
        return 15

class MilitaryCarSeat(Seat):
    def getName(self):
        return "Total Seats : " + str(self.totalSeats()) 

    def totalSeats(self):
        return 7



class AC(ABC):
    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def cost(self):
        pass

class HighPoweredAC(AC):
    def getName(self):
        return "AC : High Powered "

    def cost(self):
        return 10

class LowPoweredAC(AC):
    def getName(self):
        return "AC : Low Powered "

    def cost(self):
        return 5

