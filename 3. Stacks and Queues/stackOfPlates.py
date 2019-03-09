# Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack). 


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

class SetOfStacks:
	def __init__(self, capacity):
		self.stacks = []
		self.capacity = capacity

	def push(self, val):
		top = self.peek()
		if top and self.isMaxCapacity() == False:
			top.push(val)
		else:
			newStack = Stack()
			newStack.push(val)
			self.stacks.append(newStack)
	def pop(self):
		top = self.peek()
		if (top.isEmpty()):
			self.stacks.pop()
			top = self.peek()
		return top.pop()

	def isMaxCapacity(self):
		top = self.peek()
		if (top == False or len(top.items) == self.capacity):
			return True
		return False
	def peek(self):
		if self.isEmpty():
			return False
		last_index = len(self.stacks) - 1
		return self.stacks[last_index]

	def isEmpty(self):
		return len(self.stacks) == 0
