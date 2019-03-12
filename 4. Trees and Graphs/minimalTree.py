# Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height. 

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def minimalTree(array):
	#base case
	if len(array) == 0:
		return None
	#the middle value of a sorted rray should be at the root of the tree
	middle_index = len(array)//2
	val = array[middle_index]
	middle_node = Node(val)

	#recurse on the sub-arrays to the left and right of the middle of the current array
	middle_node.left = minimalTree(array[0:middle_index])
	middle_node.right = minimalTree(array[middle_index+1:])
	return middle_node