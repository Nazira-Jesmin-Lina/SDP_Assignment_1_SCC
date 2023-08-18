from enum import Enum


class CarType(Enum):
    RACING = 1
    PRIVATE = 2
    SUV = 3
    MILITARY = 4

class BudgetType(Enum):
    LOW = 1
    MEDIUM_LOW = 2
    MEDIUM_HIGH = 3
    HIGH = 4

class CarColor(Enum):
    RED = 1
    GRAY = 2
    BLACK = 3
    WHITE = 4