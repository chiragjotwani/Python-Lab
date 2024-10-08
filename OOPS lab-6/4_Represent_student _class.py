class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def displayinfo(self):
        print(f"Name: {self.name}, Age:{self.age}")
        
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("Charlie", 19)

student1.displayinfo()
student2.displayinfo()
student3.displayinfo()