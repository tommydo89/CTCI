# Implement a function to check if a linked list is a palindrome. 

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

Node1 = Node(1)
Node2 = Node(0)
Node3 = Node(1)
Node1.next = Node2
Node2.next = Node3


# def palindrome(node):
# 	reversed_LL = palindrome_recursion(node)
# 	while (reversed_LL.head != None or node != None):
# 		if (reversed_LL.val != node.val):
# 			return False
# 	return True

# def palindrome_recursion(node):
# 	newNode = Node(node.val)
# 	if (node.next == None):
# 		LL = LinkedList()
# 		return LL.append(newNode)
# 	result = palindrome_recursion(node.next)
# 	return result.append(newNode)

def palindrome(node):
	reversed_LL = reverseAndClone(node)
	while (node != None and reversed_LL != None):
		if (node.val != reversed_LL.val):
			return False
		node = node.next
		reversed_LL = reversed_LL.next
	return True

def reverseAndClone(node):
	head = None
	while (node != None):
		nodeClone = Node(node.val)
		if (head != None):
			nodeClone.next = head
		head = nodeClone
		node = node.next
	return head


