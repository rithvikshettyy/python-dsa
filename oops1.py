class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello World")    

    def average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "Your avg score is:", sum/3)  

s1 = Student("Aryan", [95, 98, 99])    
s1.average()    

s1.name = "Aryan Kumar"
s1.average()
s1.hello()