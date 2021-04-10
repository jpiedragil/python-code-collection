# car_dc.py
# Source code fro Medium's article
# "Why you should start using Python Dataclasses" (https://bit.ly/3fWMr2T)
# written by # Dinesh Kumar K B (https://bit.ly/3wJ1PWx)
#

from dataclasses import dataclass


@dataclass
class Car:

    name: str
    make: str
    year: int
    vehicle_type: str


car = Car("Jazz", "Honda", 2008, "Hatch")

print(car)

print(car.name)
print(car.make)
print(car.year)

print(car == Car("Jazz", "Honda", 2008, "Hatch"))
