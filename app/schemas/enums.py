from enum import Enum


class Tariffs(str, Enum):
    BASIC = "basic"
    STANDART = "standart"
    PREMIUM = "premium"


class CarTypes(str, Enum):
    CAR = "car"
    VAN = "van"
    TRUCK = "truck"
