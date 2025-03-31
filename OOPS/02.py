#add a name to the car class that displays the brand and the model of car

class Car:
    
    def __init__(self,inputbrand,inputmodel):
        self.brand = inputbrand
        self.model = inputmodel

    def display(self):
        print("The name of and car brand is :",self.brand ,"and the name of the model is :",self.model)
car1=Car("Toyota","Corolla")
car1.display()