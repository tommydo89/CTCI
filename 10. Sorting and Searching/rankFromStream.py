#  Imagine you are reading in a stream of integers. Periodically, you wish to be able
# to look up the rank of a numberx (the number of values less than or equal to x). lmplementthe data
# structures and algorithms to support these operations. That is, implement the method track ( int
# x), which is called when each number is generated, and the method getRankOfNumber(int
# x), which returns the number of values less than or equal to x (not including x itself). 
# EXAMPLE
# Stream (in order of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3
# getRankOfNumber(l) = 0
# getRankOfNumber(3) = 1
# getRankOfNumber(4) = 3 





class Node:

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.count = 0

class BST:
	
	def __init__(self):
		self.head = None

	def track(self, val):
		node = Node(val)
		if self.head == None:
			self.head = node
		else:
			temp_node = self.head # clones a reference to the head node of the BST
			while temp_node != None:
				if node.val <= temp_node.val:
					self.increment(temp_node.right) # increment all the counts of the nodes on the right since val is less than the current node 
					if temp_node.left == None: # if left is null, that means we can place the node here
						node.count = temp_node.count
						temp_node.left = node
						temp_node.count += 1
						break
					else: # else increment the count of the current node and then traverse left
						temp_node.count += 1
						temp_node = temp_node.left
				else:
					if temp_node.right == None: # if right is null, that means we can place the node here
						node.count = temp_node.count + 1
						temp_node.right = node
						break
					else: # else traverse right but first make sure the right count is 1 greater than the current node
						temp_node.right.count = temp_node.count + 1
						temp_node = temp_node.right

	def getRankOfNumber(self, val): # traverses the BST and looks for the specified val and returns its count upon finding it
		temp_node = self.head
		while temp_node != None:
			if temp_node.val == val:
				return temp_node.count
			if val < temp_node.val:
				temp_node = temp_node.left
			else:
				temp_node = temp_node.right
		return False # return False if we each the end of the BST which means the val does not exist in this tree


	def increment(self, node): # increments the count of every node in the subtree of the specified node
		if node != None:
			node.count += 1
			self.increment(node.left)
			self.increment(node.right)
# example BST
BST = BST()
BST.track(4)
BST.track(2)
BST.track(1)
BST.track(3)
BST.track(5)
#   4
#  2 5
# 1 3