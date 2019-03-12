# Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes. 


class Node:
	def __init__(self, val):
		self.val = val
		self.adjacent = []
		self.visited = False

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

	def enqueue(self, val):
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

# Directed Graph
# A -> B -> C
NodeA = Node('A')
NodeB = Node('B')
NodeC = Node('C')
NodeA.adjacent.append(NodeB)
NodeB.adjacent.append(NodeC)

def routeBetweenNodes(Node1, Node2):
	Node1toNode2 = routeExists(Node1, Node2)
	Node2toNode1 = routeExists(Node2, Node1)
	if (Node1toNode2 or Node2toNode1):
		return True
	return False

def routeExists(start, end):
	queue = MyQueue()
	queue.enqueue(start)
	while (not queue.isEmpty()):
		poppedNode = queue.dequeue()
		poppedNode.visited = True
		if (poppedNode == end):
			return True
		for node in poppedNode.adjacent:
			if (node.visited == False):
				queue.enqueue(node)
	return False


