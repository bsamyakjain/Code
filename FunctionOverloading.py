#No function overloading is possible in Python

class Employee:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation

    def demo(n,m):
        print("First demo")
    def demo(n):
        print("second demo")


try:
    Employee.demo(2,3)
except:
    Employee.demo(2)

# always the last one is exceuted
