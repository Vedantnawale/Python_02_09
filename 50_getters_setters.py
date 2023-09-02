# class MyClass:
#     def __init__(self,value):
#         self._value= value
#     def show(self):
#         print(f"Value is {self._value}")
#     @property
#     def ten_value(self):
#         return  10*self._value
    
#     @ten_value.setter
#     def ten_value(self,new_value):
#         self._value = new_value/10
    
# obj = MyClass(10)
# obj.ten_value = 67
# print(obj.ten_value)
# obj.show()
# Python program showing a
# use of property() function

class Geeks:
	def __init__(self):
		self._age = 0
	
	# function to get value of _age
	def get_age(self):
		print("getter method called")
		return self._age
	
	# function to set value of _age
	def set_age(self, a):
		print("setter method called")
		self._age = a

	# function to delete _age attribute
	def del_age(self):
		del self._age
	
	age = property(get_age, set_age, del_age)

mark = Geeks()

mark.age = 10

print(mark.age)
