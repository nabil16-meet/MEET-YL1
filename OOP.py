class Animal:
	def __init__(self, name, age, color, size):
		self.name = name
		self.age = age
		self.color = color
		self.size = size
Dog = Animal("kookoo", 22, "Yellow", "tiny")
print (Dog.name)
print (Dog.age)
print (Dog.color)
print (Dog.size)
