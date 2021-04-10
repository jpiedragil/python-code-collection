# car_dc01.py
# Source code fro Medium's article
# "Why you should start using Python Dataclasses" (https://bit.ly/3fWMr2T)
# written by # Dinesh Kumar K B (https://bit.ly/3wJ1PWx)
#

from dataclasses import dataclass, is_dataclass, make_dataclass, fields, \
     asdict, astuple


@dataclass
class Car:

    name: str
    make: str
    year: int
    vehicle_type: str


car = Car("Jazz", "Honda", 2008, "Hatch")

car.year = 2019

print(car)
