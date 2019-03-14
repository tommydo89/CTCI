# Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions. 

class LinkedList:
	def __init__(self):
		self.head = None
		self.end = None
	def append(self, val):
		newNode = Node(val)
		if self.head == None:
			self.head = newNode
		else:
			self.end.next = newNode
		self.end = newNode

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def partition(node, k):
	beforeNodes = LinkedList()
	afterNodes = LinkedList()
	while node != None:
		if (node.val < k):
			beforeNodes.append(node.val)
		else:
			afterNodes.append(node.val)
		node = node.next
	beforeNodes.end.next = afterNodes.head
	return beforeNodes



Node1 = Node(5)
Node2 = Node(4)
Node3 = Node(3)
Node4 = Node(2)
Node5 = Node(1)
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5






