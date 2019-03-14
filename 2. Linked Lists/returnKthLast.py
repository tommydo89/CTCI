 # Implement an algorithm to find the kth to last element of a singly linked list. 

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None


Node1 = Node(5)
Node2 = Node(5)
Node3 = Node(10)
Node1.next = Node2
Node2.next = Node3

# def returnKthLast(node, k):
# 	if (node == None):
# 		return 0
# 	index = returnKthLast(node.next, k) + 1
# 	if (index == k ):
# 		print('The kth to last node is %d' % node.val)
# 	return index

def returnKthLast(node, k):
	if (node == None):
		return 1
	# result will either be an index or the kth last node
	result = returnKthLast(node.next, k)
	# if val is a property of result, that means result is the kth last node and so we want to return result
	if (not isinstance(result, int)):
		return result
	# result is not a node, that means it is an index and so we check to see if it is the kth index and return node if it is
	if (result == k ):
		return node
	# if neither of the conditions above are met, then we return index + 1 
	return result + 1
