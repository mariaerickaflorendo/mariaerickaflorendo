class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am studying {self.course}.")

# Creating three student objects
student1 = Student("Marai Ericka Florendo", 23, "DIP-IT II")
student2 = Student("Jannele Chua", 27, "DIP-IT II")
student3 = Student("Jhen Senado", 27, "DIP-IT II")

# Calling the introduce method for each student
student1.introduce()
student2.introduce()
student3.introduce()
