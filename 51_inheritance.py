class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")


e = Employee("Rohan Das", 400)
e.showDetails()
e2 = Programmer("Vedant", 786)
e2.showDetails()
e2.showLanguage()

# Inherittance Employee --> Programmer
# Inherritance mhnje relationship between parents and child child uses parents parameter
# It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
