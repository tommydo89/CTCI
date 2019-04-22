# An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in Linked list data structure


class Node:
	def __init__(self, val):
		self.val = val
		self.next = None


class AnimalShelter:

	def __init__(self):
		self.head = None
		self.end = None


	def enqueue(self, val):
		if (val != 'Dog' and val != 'Cat'):
			return False
		newAnimal = Node(val)
		if (self.head == None):
			self.head = newAnimal
		else:
			self.end.next = newAnimal
		self.end = newAnimal

	def dequeueAny(self):
		if (self.head == None):
			return False
		animal = self.head
		self.head = self.head.next
		if (self.head == None):
			self.end = None
		return animal

	def dequeueDog(self):
		animal = self.head
		if (animal.val == 'Dog'):
			self.head = self.head.next
			return animal
		while (animal.next != None):
			if (animal.next.val == 'Dog'):
				if (animal.next == self.end):
					self.end = animal
				returnAnimal = animal.next
				animal.next = animal.next.next
				return returnAnimal
			animal = animal.next

	def dequeueCat(self):
		animal = self.head
		if (animal.val == 'Cat'):
			self.head = self.head.next
			return animal
		while (animal.next != None):
			if (animal.next.val == 'Cat'):
				if (animal.next == self.end):
					self.end = animal
				returnAnimal = animal.next
				animal.next = animal.next.next
				return returnAnimal
			animal = animal.next
