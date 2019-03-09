# Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty. 

class Stack:
	def __init__(self):
		self.items = []

	def push(self, val):
		self.items.append(val)

	def pop(self):
		if self.isEmpty():
			return False
		return self.items.pop()

	def isEmpty(self):
		return len(self.items) == 0

	def peek(self):
		if self.isEmpty():
			return False
		last_index = len(self.items) - 1
		return self.items[last_index]

def sortStack(stack):
	sortedStack = Stack()
	while (not stack.isEmpty()):
		val = stack.pop()
		insertIntoSorted(val, sortedStack)
	return sortedStack

def insertIntoSorted(val, sortedStack):
	if sortedStack.isEmpty():
		sortedStack.push(val)
		return		
	if (val < sortedStack.peek()):
		sortedStack.push(val)
		return
	temp = sortedStack.pop()
	insertIntoSorted(val, sortedStack)
	sortedStack.push(temp)
	return
	