class Student:
    def __init__(self, name):
        self.name = name
        self._marks = []

    def add_marks(self, mark):
        if 0 <= mark <= 100:
            self._marks.append(mark)
        else:
            print("Invalid mark. Please enter a value between 0 and 100.")

    def get_average_marks(self):
        if self._marks:
            return sum(self._marks) / len(self._marks)
        else:
            return 0

    def display_marks(self):
        print(f"Marks for {self.name}: {self._marks}")

if __name__ == "__main__":
    student1 = Student("Alice")
    student1.add_marks(85)
    student1.add_marks(90)
    student1.add_marks(78)
    student1.display_marks()
    average = student1.get_average_marks()
    print(f"Average marks for {student1.name}: {average:.2f}")