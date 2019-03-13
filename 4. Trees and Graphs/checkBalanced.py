# Implement a function to check if a binary tree is balanced. For the purposes of
# this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one. 

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None

# Balanced Tree
Node1 = TreeNode(1)
Node2 = TreeNode(2)
Node3 = TreeNode(3)
Node1.left = Node2
Node1.right = Node3

#Unbalanced Tree
Node4 = TreeNode(4)
Node5 = TreeNode(5)
Node6 = TreeNode(6)
Node4.left = Node5
Node5.left = Node6

def checkBalanced(tree):
	return recursiveCheck(tree) != False

def recursiveCheck(treeNode):
	#base case
	if treeNode == None:
		return 1

	#these values will either be an integer representing the depth of the left and right sub trees of the current node, or it will be False if we have discovered it is not balanced
	left_subtree_depth = recursiveCheck(treeNode.left)
	right_subtree_depth = recursiveCheck(treeNode.right)

	# repeatedly returns False once we discover that it is not balanced
	if (left_subtree_depth == False or right_subtree_depth == False):
		return False

	# returns False upon discovering imbalance
	if (abs(left_subtree_depth - right_subtree_depth) > 1):
		return False

	# the depth of a tree is 1 plus the larger depth of it's left and right sub trees
	if (left_subtree_depth > right_subtree_depth):
		return left_subtree_depth + 1
	else:
		return right_subtree_depth + 1