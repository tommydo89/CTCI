# Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists). 

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None

class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.end = None

	def append(self, val):
		newNode = ListNode(val)
		if (self.head == None):
			self.head = newNode
		else:
			self.end.next = newNode
		self.end = newNode

Node1 = TreeNode(1)
Node2 = TreeNode(2)
Node3 = TreeNode(3)
Node1.left = Node2
Node1.right = Node3

def listOfDepths(tree):
	depth_dict = {}
	result = recursiveDepths(tree, depth_dict, 0)
	return depth_dict


def recursiveDepths(treeNode, depth_dict, current_depth):
	if treeNode == None:
		return
	recursiveDepths(treeNode.left, depth_dict, current_depth + 1)
	recursiveDepths(treeNode.right, depth_dict, current_depth + 1)
	depth_dict[current_depth] = depth_dict.get(current_depth, LinkedList())
	depth_dict[current_depth].append(treeNode.val)

