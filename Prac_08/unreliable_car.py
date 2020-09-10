from Prac_08.car import Car
from random import randint
class UnreliableCar(Car):
    def __init__(self,name,fuel,reliablity):
        super().__init__(name,fuel)
        self.reliablity = reliablity
    def drive(self, distance):
        drvie_percentage = randint(0,100)
        distance_driven=0
        if self.reliablity>drive_percentage:
            distance_driven=super().drive(distance)
        return distance_driven