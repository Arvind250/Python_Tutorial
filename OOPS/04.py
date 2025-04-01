#counting the number of objects created

class Car:
    total = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total += 1
    def count():
        print("The total count is : ",Car.total)


car1 = Car("Toyota","corolla")
car2 = Car("new","new_model")
car3 = Car("car","model")
Car.count()