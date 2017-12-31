class Animal(object):
	pass

class Mammal(Animal):
	pass

class Runnable(object):
	def run(self):
		print("I am running....")

class Flyable(object):
	def fly(self):
		print("I am flying....")	

class Bird(Animal,Flyable):
	pass

class Dog(Mammal,Runnable):
	pass

class Parrot(Bird):
	pass


