#methods : Class, instance, static

class Employee:
    """This is a Employee class contains breif of methods"""
    #class variable
    class_variable = "This is class Variable"

    def __init__(self,name):
        self.name = name #instance variable

    def this_is_instance_method(self): #instance method which contains self as first arguemnts
        print(self.name)

    @classmethod
    def this_class_method(cls):
        print(cls.class_variable)

    @staticmethod
    def this_static_method():
        print("contains no relationship betweem class or instane variable")
        
e1= Employee("This is instance method")
e1.this_is_instance_method()

Employee.this_class_method()
print(Employee.class_variable)

from SamyakLib import *
stars()

Employee.this_static_method()
print(Employee.__doc__)

stars()

#access modifier:
class cars:

    def __init__(self, name,salary):
        self.__name = name
        self.salary = salary

    def __display(self):
        print(self.__name,self.salary)


c1 = cars("Samyak", 60000)
c1.salary = 40000

c1._cars__display()

#we can access them using _class
c1._cars__name = "mark"
print()

#so there are only public and private.


#Inheritance
