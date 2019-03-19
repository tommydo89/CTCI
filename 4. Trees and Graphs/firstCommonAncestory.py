# Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
# necessarily a binary search tree. 

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)
Node1.left = Node2
Node2.left = Node3
Node2.right = Node4
Node4.left = Node5
#   1
#  2
# 3 4

def recursiveSearch(node, node1, node2):
	# base case is either reaching the end of the tree, or upon finding one of the nodes
	if (node == None):
		return False
	if (node == node1 or node == node2):
		return True

	# if above conditions are not met, recurse on the left and right node
	left = recursiveSearch(node.left, node1, node2)
	right = recursiveSearch(node.right, node1, node2)

	# if either the left or right are not a boolean, that means we have found the common ancestor node so just return the node
	if (not isinstance(left, bool)):
		return left
	if (not isinstance(right, bool)):
		return right

	# if left and right are true, that mean's this node is the common ancestor so return the node
	if (left and right):
		return node

	# if left or right is true, that means one of the nodes exists in this subtree
	if (left or right):
		return True

	# return False if neither the left or right subtree of this node contains any of the nodes we are looking for
	return False
