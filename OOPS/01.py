class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
car1 = Car("Toyota","Corolla")
print(car1.brand,car1.model)
car2 = Car("Tata","Safari")
print(car2.brand,car2.model)