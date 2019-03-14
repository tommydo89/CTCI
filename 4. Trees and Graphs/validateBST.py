# Implement a function to check if a binary tree is a binary search tree. 


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None

# Valid BST
Node1 = TreeNode(1)
Node2 = TreeNode(2)
Node3 = TreeNode(3)
Node4 = TreeNode(4)
Node3.left = Node2
Node3.right = Node4
Node2.left = Node1
# Result
#   3
#  2 4
# 1

# Invalid BST
Node5 = TreeNode(5)
Node6 = TreeNode(6)
Node5.left = Node6


def validateBST(tree):
	return recursiveTraverse(tree) not in [False, None]

def recursiveTraverse(node):
	# base case
	if (node == None):
		return 

	# these left_val and right_val will either be a
		# Int: val of left/right child 
		# False: indicating it is not a BST
		# None: return of the base case
	left_val = recursiveTraverse(node.left)
	right_val = recursiveTraverse(node.right)

	# repeatedly return False once we validate the tree is not a BST
	if (left_val == False or right_val == False):
		return False
	# if the above check for False fails, check to see that these values are not None which means they are ints, and then check if their values hold the properties of a BST
	if (left_val and left_val > node.val):
		return False
	if (right_val and right_val < node.val):
		return False
	# return the value of the node if it is not the base case and BST properties are held
	return node.val
