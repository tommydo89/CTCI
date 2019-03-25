# You are implementing a binary search tree class from scratch, which, in addition
# to insert, find, and delete, has a method getRandomNode() which returns a random node
# from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
# for getRandomNode, and explain how you would implement the rest of the methods. 

import random

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None
		self.size = 1

class BST:
	def __init__(self):
	 	self.head = None

	def insertNode(self, val, node = None):
		# default value for node is head
		node = node if node is not None else self.head
		# if the BST is empty, set head to be the new node
		if (self.head == None):
			self.head = TreeNode(val)
			return
		# insert the node to the right or left depending on if its greater than or less than the current node
		if (val < node.val):
			if node.left == None:
				node.left = TreeNode(val)
			else:
				self.insertNode(val,node.left)
		if (val >= node.val):
			if node.right == None:
				node.right = TreeNode(val)
			else:
				self.insertNode(val, node.right)
		node.size += 1

	def getRandomNode(self, node = None):
		# default value for node is head
		node = node if node is not None else self.head

		# if tree is empty, return none
		if (node == None):
			return None

		# if left subtree is empty, the middle index (index representing root node) of the tree is 0 else it is the size of the left subtree
		middle_index = node.left.size if node.left is not None else 0

		# randomly select an index. If the index is equal to the middle index, return the current node, else recurse on left if the index < middle index or the right if the index > middle index
		index = random.randint(0, node.size - 1)
		if (index < middle_index):
			return self.getRandomNode(node.left)
		if (index == middle_index):
			return node
		else:
			return self.getRandomNode(node.right)

BST = BST()
BST.insertNode(2)
BST.insertNode(1)
BST.insertNode(3)