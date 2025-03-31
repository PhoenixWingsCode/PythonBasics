class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class ToyotaCar(Car):
    def __init__(self, brand, type):
        super().__init__(type)
        self.brand = brand
        super().start()

car1 = ToyotaCar("innova","electric")
print(car1.type)        