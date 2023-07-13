class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi oluşturuldu")

    def info(self):
        print(self.name,self.surname,self.age)

    

class Student(Person):
    pass

class Teacher(Person):
    pass

person_1 = Person("Yagmur","Ozturk",20)
print(person_1.name,person_1.surname,person_1.age)
student_1 = Student("Zeynep","Yilmaz",12)
print(student_1.name,student_1.surname,student_1.age)
teacher_1 = Teacher("Ayça","Yilmaz",34)
print(teacher_1.name,teacher_1.surname,teacher_1.age)

person_1 = Person("Yagmur","Ozturk",20)
person_1.info()
student_1 = Student("Zeynep","Yilmaz",12)
student_1.info()
teacher_1 = Teacher("Ayça","Yilmaz",34)
teacher_1.info()


