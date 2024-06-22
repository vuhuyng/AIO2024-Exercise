import q6_teacherclass
import q7_doctorclass
import q5_studentclass


class Ward:
    def __init__(self, name: str):
        self.__name = name
        self.__listpeople = list()

    def add_person(self, person):
        self.__listpeople.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self.__listpeople:
            p.describe()

    def count_doctor(self):
        return sum(isinstance(p, q7_doctorclass.Doctor) for p in self.__listpeople)


student1 = q5_studentclass.Student(name="studentA", yob=2010, grade="7")
teacher1 = q6_teacherclass.Teacher(name="teacherA", yob=1969, subject="Math")
teacher2 = q6_teacherclass.Teacher(
    name="teacherB", yob=1995, subject="History")
doctor1 = q7_doctorclass.Doctor(
    name="doctorA", yob=1945, specialist="Endocrinologists")
doctor2 = q7_doctorclass.Doctor(
    name="doctorB", yob=1975, specialist="Cardiologists")

ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

assert ward1.count_doctor() == 2
ward1.count_doctor()
