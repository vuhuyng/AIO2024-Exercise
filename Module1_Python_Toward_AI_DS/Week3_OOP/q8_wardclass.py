class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        print(f"Name: {self.name}, Year of Birth: {self.yob}")


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        super().describe()
        print(f"Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        super().describe()
        print(f"Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        super().describe()
        print(f"Specialist: {self.specialist}")


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__listPeople = []

    def add_person(self, person):
        self.__listPeople.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self.__listPeople:
            p.describe()

    def count_doctor(self):
        return sum(1 for p in self.__listPeople if isinstance(p, Doctor))


student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologist")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologist")

ward1 = Ward(name="Ward1")

ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

ward1.describe()

print(f"Number of doctors: {ward1.count_doctor()}")
