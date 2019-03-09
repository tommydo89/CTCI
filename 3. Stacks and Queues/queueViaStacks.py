# Implement a MyQueue class which implements a queue using two stacks


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

class MyQueue:
	def __init__ (self):
		self.queue = Stack()
		self.helper_stack = Stack()

	def queue(self, val):
		while (not self.queue.isEmpty()):
			self.helper_stack.push(self.queue.pop())
		self.helper_stack.push(val)
		while (not self.helper_stack.isEmpty()):
			self.queue.push(self.helper_stack.pop())
	def dequeue(self):
		if self.isEmpty():
			return False
		return self.queue.pop()

	def peek(self):
		return self.queue.peek()

	def isEmpty(self):
		return self.queue.isEmpty()
