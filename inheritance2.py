class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi oluşturuldu")

    def info(self):
        print(self.name, self.surname, self.age)


class Student(Person):
    def __init__(self, name, surname, age, number):
        super().__init__(name, surname, age)
        self.number = number
        print("student nesnesi oluşturuldu")


class Teacher(Person):
    def __init__(self, name, surname, age, branch):
        super().__init__(name, surname, age)
        self.branch = branch
        print("teacher nesnesi oluşturuldu")

    def teach(self):
        print(
            f"{self.name} {self.surname} isimli öğretmen {self.branch} eğitimi vermektedir.")


person_1 = Person("Yagmur", "Ozturk", 20)
person_1.info()
student_1 = Student("Zeynep", "Yilmaz", 12, 344)
student_1.info()
print(student_1.number)
teacher_1 = Teacher("Ayça", "Yilmaz", 34, "fizik")
teacher_1.info()
print(teacher_1.branch)

teacher_1.teach()
