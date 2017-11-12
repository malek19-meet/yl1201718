class Animal(object):
	def __init__(self,sound,name,age,favourite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favourite_color = favourite_color
	def eat(self,food):
		print("YUMMY!!  " + self.name + "is eating " + food)
	def description(self):
		print(self.name + "is" + self.age + "years old and loves the color " + self.favourite_color)
m = Animal("miaw","cat ","14","orange")
m.eat("fish")
