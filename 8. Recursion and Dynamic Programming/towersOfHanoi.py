# In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
# different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
# of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following
# constraints:

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

stackA = Stack()
stackB = Stack()
stackC = Stack()

stackA.push(5)
stackA.push(4)
stackA.push(3)
stackA.push(2)
stackA.push(1)

def towersOfHanoi(size, from_stack, to_stack, aux_stack):
	# think of each call to towersOfHanoi as it's own sub problem. Only when the number of rings to move is equal to 1 do we actually move the ring from from_stack _> to_stack

	if size == 1:
		to_stack.push(from_stack.pop())
		return
	towersOfHanoi(size-1, from_stack, aux_stack, to_stack) # in order to get the bottom ring to the last stack, you must move the rings on top of it from the first stack, to the aux stack
	to_stack.push(from_stack.pop()) # now that the largest ring is free to move, we move it onto the last stack
	towersOfHanoi(size-1, aux_stack, to_stack, from_stack) # we then want to move all the rings on the aux stack onto the last stack

