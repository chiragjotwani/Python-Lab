class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age
        self.__salary = salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Age: {self._age}")
        print(f"Employee Salary: {self.get_salary()}")

if __name__ == "__main__":
    emp1 = Employee("John Doe", 30, 50000)
    
    emp1.display_details()
    
    emp1.set_salary(55000)
    print("Updated Salary:")
    emp1.display_details()