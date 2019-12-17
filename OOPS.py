## How to make class, methods and objects


class Employee:
    id = 10
    name = "Nishit"

    def display(self):
        print("Id :" + str(self.id) + "\n Name:" + self.name)


obj1 = Employee()
obj1.display()
#################################################################
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
##################################################################
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
####################################################################
## Multilevel inheritance


# class Animal:
#     def method_animal(self):
#         print("Method of class Animal called")
#     # The child class Dog inherits the base class Animal
#
#
# class Dog(Animal):
#     def method_dog(self):
#         print("Method of class Dog called")
#     # The child class Dogchild inherits another child class Dog
#
#
# class Puppy(Dog):
#     def method_puppy(self):
#         print("Method of class Puppy called")
#
#
# puppy1 = Puppy()
# puppy1.method_animal()
# puppy1.method_dog()
# puppy1.method_puppy()
#########################################################
# Multiple Inheritance


# class Sum:
#     def Summation(self, a, b):
#         return a + b;


# class Mul:
#     def Multiplication(self, a, b):
#         return a * b;


# class Derived(Sum, Mul):
#     def Divide(self, a, b):
#         return a / b;


# d = Derived()
# print(d.Summation(10, 20))
# print(d.Multiplication(10, 20))
# print(d.Divide(10, 20))
#########################################################
## Use of polymorphism

class Bank:
    def getroi(self):
        return 10


class SBI(Bank):
    def getroi(self):
        return 7


class ICICI(Bank):
    def getroi(self):
        return 8


b1 = Bank()
b2 = SBI()
b3 = ICICI()
print("Bank Rate of interest:", b1.getroi())
print("SBI Rate of interest:", b2.getroi())
print("ICICI Rate of interest:", b3.getroi())
##########################################################
# Method overloading

# class A:
#     def add(self, x, y):
#         return x + y

#     def add(self, x, y, z):
#         return x + y + z


# obj = A()
# print(obj.add(1, 2,3))
# print(obj.add(1, 2, 5))
##########################################################
# # Method Overriding

# class A:

#     def show(self):
#         print("A's show")


# class B():
#
#     def show(self):
#         print("B's show")


# obj1 = A()
# obj1.show()
# obj2 = B()
# obj2.show()
##############################################################
