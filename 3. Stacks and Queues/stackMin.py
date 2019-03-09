# How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prevMin = None

class Stack:
	def __init__(self):
		self.items = []
		self.min = None

	def push(self, val):
		newNode = Node(val)
		if (self.min == None or val < self.min):
			newNode.prevMin = self.min
			self.min = val
		self.items.append(newNode)

	def pop(self):
		if self.isEmpty():
			return False
		poppedNode = self.items.pop()
		if self.isEmpty():
			self.min = None
		if poppedNode.prevMin:
			self.min = poppedNode.prevMin
		return poppedNode

	def isEmpty(self):
		return len(self.items) == 0

	def peek(self):
		if self.isEmpty():
			return False
		last_index = len(self.items) - 1
		return self.items[last_index]

	def getMin(self):
		if self.min == None:
			return False
		return self.min
