# car.py
# Source code fro Medium's article
# "Why you should start using Python Dataclasses" (https://bit.ly/3fWMr2T)
# written by # Dinesh Kumar K B (https://bit.ly/3wJ1PWx)
#

class Car(object):

    def __init__(self, name: str, make: str, year: int, vehicle_type: str):

        """
        :param name: Name of the car
        :param make: Brand(Hyundai/Toyota)
        :param: year: Making year
        :param: vehicle_type: Sedan/SUV/Hatch
        """

        self.name = name
        self.make = make
        self.year = year
        self.vehicle_type = vehicle_type


car = Car("Jazz", "Honda", 2008, "Hatch")

print(car.make)
print(car.name)
print(car)
