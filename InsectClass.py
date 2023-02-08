import random


class Insect:
    def __init__(self):
        self.wings = "2"
        self.legs = "4"
        self.flight_length = "0"

    def flight(self):
        self.flight_length = random.randint(0, 10)

    def get_flight(self):
        return self.flight_length
