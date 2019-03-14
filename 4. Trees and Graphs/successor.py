# Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
# binary search tree. You may assume that each node has a link to its parent.


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None
		self.parent = None

#BST
Node1 = TreeNode(1)
Node2 = TreeNode(2)
Node3 = TreeNode(3)
Node4 = TreeNode(4)
Node5 = TreeNode(5)
Node4.left = Node2
Node2.parent = Node4
Node4.right = Node5
Node5.parent = Node4
Node2.left = Node1
Node1.parent = Node2
Node2.right = Node3
Node3.parent = Node2

#Result
#	4
#  2 5
# 1 3

def successor(treeNode):
	if treeNode.right:
		return traverseLeft(treeNode.right)
	else:
		return traverseParent(treeNode.parent, treeNode.val)


def traverseLeft(node):
	while (node.left != None):
		node = node.left
	return node

def traverseParent(parent, val):
	while (parent!= None):
		if (parent.val > val):
			return parent
		parent = parent.parent
	return False
		