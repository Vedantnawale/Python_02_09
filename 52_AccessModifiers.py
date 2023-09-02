class Employee:
   def __init__(self):
    #   self.name = "Om"
      self.__name = "Om"

a = Employee()
# print(a.name)  # Public Modifier
# print(a.__name)  # Cannot be accesed directly
print(a._Employee__name)  # Private Modifier Can be accessed directly

# Name Mangling
print(a.__dir__())

# Protected (_)