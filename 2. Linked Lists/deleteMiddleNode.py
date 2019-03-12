# Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node. 

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None


Node1 = Node(5)
Node2 = Node(5)
Node3 = Node(10)
Node4 = Node(20)
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4


def deleteMiddleNode(node):
	if (node == None or node.next == None):
		return False
	nextNode = node.next
	node.val = nextNode.val
	node.next = nextNode.next
	return True
	