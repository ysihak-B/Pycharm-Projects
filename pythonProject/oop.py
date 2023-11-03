# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         print("bark")
#
#     def add_one(self, x):
#         return x + 1
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         self.age = age
#
#
# d = Dog("kalab", 4)
# d.bark()
# d.set_age(25)
# print(d.get_name())
# print(d.get_age())
# print(d.add_one(5))
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_student = max_students
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_student:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        su = 0
        for student in self.students:
            su = su + student.get_grade()
        return su / len(self.students)


stu1 = Student("kale ab", 13, 90)
stu2 = Student("abel", 19, 95)
stu3 = Student("abuchu", 5, 75)

course = Course("cyber", 2)
course.add_students(stu1)
course.add_students(stu2)

print(course.add_students(stu3))
print(course.get_average_grade())