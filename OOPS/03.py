class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model,battery):
        super().__init__(brand, model)
        self.battery = battery

car1 = Car("Toyota","corolla")
print(car1.brand,car1.model)
car2 = ElectricCar("Tesla","Model S","80KWh")
print(car2.brand,car2.model,car2.battery)