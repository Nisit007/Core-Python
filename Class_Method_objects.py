##### How to make class, methods and objects
class Employee:
    id = 10
    name = "Nishit"

    def display(self):
        print("Id :" + str(self.id) + "\n Name:" + self.name)


obj1 = Employee()
obj1.display()
###################################################################
# class Student:
#     count = 0
#
#     def __init__(self):
#         Student.count = Student.count + 1
#         # print("Constructor called")
#
#
# s1 = Student()
# s2 = Student()
# s3 = Student()
# s4 = Student()
# print("The number of students:", Student.count)
####################################################################
# Parameterized constructor

class Student:
    # Constructor - parameterized
    def __init__(self, name, name1):
        print("This is parametrized constructor")
        self.name = name
        self.name1 = name1

    def show(self):
        print("Hello", self.name)
        print("hello", self.name1)


student = Student("John", "nishit")
student.show()
######################################################################
