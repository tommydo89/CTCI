# Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
# algorithm to determine ifT2 is a subtree of Tl.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
Node5 = TreeNode('C')
Node1 = TreeNode('A')
Node2 = TreeNode('B')
Node5.left = Node1
Node1.left = Node2

Node3 = TreeNode('A')
Node4 = TreeNode('B')
Node6 = TreeNode('D')
Node3.left = Node4
Node4.left = Node6

def checkSubtree(T1, T2):
	if (T1 == None):
		return False
	if (T1.val == T2.val):
		if treeMatch(T1, T2):
			return True
	foundLeft = checkSubtree(T1.left, T2)
	foundRight = checkSubtree(T1.right,T2)
	if (foundLeft or foundRight):
		return True
	return False

def treeMatch(T1, T2):
	if (T1 == None and T2 == None):
		return True
	if (T1 == None and T2):
		return False
	if (T2 == None and T1):
		return False
	if (T1.val != T2.val):
		return False
	if (T1.val == T2.val):
		return treeMatch(T1.left, T2.left) and treeMatch(T1.right, T2.right)
