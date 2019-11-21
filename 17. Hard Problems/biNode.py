#  Consider a simple data structure called BiNode, which has pointers to two other nodes.
# public class BiNode {
# }
# public BiNode nodel, node2;
# public int data;
# The data structure BiNode could be used to represent both a binary tree (where nodel is the left
# node and node2 is the right node) or a doubly linked list (where nodel is the previous node and
# node2 is the next node). Implement a method to convert a binary search tree (implemented with
# BiNode) into a doubly linked list. The values should be kept in order and the operation should be
# performed in place (that is, on the original data structure). 

class BiNode:

	def __init__(self, val, left, right):
		self.val = val
		self.node1 = left
		self.node2 = right



def biNode(BSTroot):
	traverse(BSTroot, BSTroot)


# main concept: we want to connect a node to the biggest number of its subarray on the left, and the smallest number of its subarray on the right.
# so at each iteration we return the smallest and biggest number of the subarray at the current node
def traverse(curr_node, root):
	if curr_node == None: # base case for reaching end of the BST
		return None, None
	left_smallest, left_biggest = traverse(curr_node.node1, root) 
	curr_node.node1 = left_biggest # sets the previous node of the current node to be the biggest valued node of its left subarray
	if (left_biggest != None): # sets the current node as the next node of the biggest valued node in its left subarray
		left_biggest.node2 = curr_node
	right_smallest, right_biggest = traverse(curr_node.node2, root)
	curr_node.node2 = right_smallest # sets the next node of the current node to be the smallest valued node of its right subarray
	if (right_smallest != None):
		right_smallest.node1 = curr_node # sets the current node as the previous node of the smallest valued node in its left subarray
	if (left_smallest == None): # smallest value of the subarray is the current node if the left is none
		left_smallest = curr_node
	if (right_biggest == None): # biggest value of the subarraay is the current node if the right is none
		right_biggest = curr_node 
	if (curr_node == root): # we have made it back to the start of recursion so just end and return nothing
		return
	return left_smallest, right_biggest # return the smallest and biggest values of the subarray at the current node


