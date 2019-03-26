# You are given a binary tree in which each node contains an integer value (which
# might be positive or negative). Design an algorithm to count the number of paths that sum to a
# given value. The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes). 

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None

Node1 = TreeNode(1)
Node2 = TreeNode(2)
Node3 = TreeNode(3)
Node4 = TreeNode(1)
Node5 = TreeNode(0)
Node6 = TreeNode(0)
Node1.left = Node2
Node1.right = Node3
Node2.left = Node4
Node3.left = Node5
Node3.right = Node6
#    1
#  2   3
# 1   0 0


# def pathsWithSum(tree, target):
# 	results = []
# 	recursiveTraverse(tree, target, results)
# 	return len(results)


# def recursiveTraverse(node, target, results):
# 	#base case
# 	if node == None:
# 		return []
# 	#recurse to the left and right
# 	left_sums = recursiveTraverse(node.left, target, results)
# 	right_sums = recursiveTraverse(node.right, target, results)

# 	#the possible sums at this current node is the value of the current node, and then the sum of that value with all the other possible values from the left and right subtree
# 	current_val = node.val
# 	sums = [current_val]
# 	for number in left_sums:
# 		if current_val + number == target:
# 			results.append(1)
# 		sums.append(current_val + number)
# 	for number in right_sums:
# 		if current_val + number == target:
# 			results.append(1)
# 		sums.append(current_val + number)
# 	return sums

def pathsWithSum(tree, target):
	pathCount = {}
	return recursiveTraverse(tree, target, pathCount)

def recursiveTraverse(node, targetSum, pathCount, runningSum = 0):
	#base case
	if node == None:
		return 0
	runningSum += node.val
	pathSum = runningSum - targetSum	
	totalPaths = pathCount.get(pathSum, 0)
	if (runningSum == targetSum):
		totalPaths += 1
	pathCount[runningSum] = pathCount.get(pathSum, 0) + 1

	totalPaths += recursiveTraverse(node.left, targetSum, pathCount, runningSum)
	totalPaths += recursiveTraverse(node.right, targetSum, pathCount, runningSum)

	return totalPaths
