class Node:
	def __init__(self, val):
		self.val = val
		self.next = None


Node1 = Node(5)
Node2 = Node(5)
Node3 = Node(10)
Node1.next = Node2
Node2.next = Node3

def returnKthLast(node, k):
	if (node == None):
		return 0
	index = returnKthLast(node.next, k) + 1
	if (index == k ):
		print('The kth to last node is %d' % node.val)
	return index
