class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
    def print_info(self):
        print(f"Name:{self.name}, Age:{self.age}")
        
person1= Person("Alice", 30)
person2=Person("Bob", 25)    

person1.print_info()
person2.print_info()