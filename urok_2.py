class Student:
    def _init_(self, name, age, IQ):
        self.name = name
        self.age = age
        self.IQ = IQ
        self.hp =100

    def printer(self):
        print("name:" + self.name)
        print("age:" + str(self.age))
        print("IQ:" + str(self.IQ))
        print("hp:" + str(self.hp))

    def to_study(self):
        print("Time to study")
        self.hp -=10
        self.IQ +=10
    def to_sleep(self):
        print("Zzzzzz....")
        self.hp +=5

    def to_chill(self):
        print("Chilling!!!")
        self +=2


first_student = Student(name = "Jamil", age = 13, IQ = 5)
second_student = Student(name = "Murad", age = 14, IQ = 1)
third_student = Student(name = "Elmir", age = 15, IQ = 160)

second_student.printer()

second_student.to_sleep()

second_student.printer()

second_student.to_study()

second_student.printer()