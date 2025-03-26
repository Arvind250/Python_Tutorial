class Student:
    def __init__(self,name,marks):
        self.name =name
        self.marks= marks
    def Print_name (self):
        print("Hello",self.name)
    def Print_avg(self):
        sum=0
        for mark in self.marks:
            sum+=mark
        avg = sum/len(self.marks)
        print("the average is : ",avg)
student1 = Student("John",[90,89,97,92,88])
student1.Print_name()
student1.Print_avg()