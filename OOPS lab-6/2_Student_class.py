class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        
    def displayinfo(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.rollno}")
        
student1=Student("John",2)
student1.displayinfo()