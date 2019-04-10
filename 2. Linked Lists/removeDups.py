# Write code to remove duplicates from an unsorted linked list. 

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None


Node1 = Node(5)
Node2 = Node(5)
Node3 = Node(10)
Node1.next = Node2
Node2.next = Node3

# def removeDups(head):
# 	thisdict = {}
# 	temp_head = head
# 	thisdict[temp_head.val] = thisdict.get(temp_head.val, 0) + 1
# 	while (temp_head.next != None):
# 		if (thisdict.get(temp_head.val, 0) > 0):
# 			temp_head.next = temp_head.next.next
# 		else:
# 			thisdict[temp_head.val] = thisdict.get(temp_head.val, 0) + 1
# 		temp_head = temp_head.next
# 	return head

def removeDups(head):
	nodeDict = {} # dictionary that keeps track of nodes that have been seen 
	temp_node = head # reference to head so that we do not change head as we are iterating through the linked list
	while (temp_node != None): # iterates each node
		if nodeDict.get(temp_node.val, 0) == 1: # if we have already seen this value, then remove it 
			removeNode(temp_node)
		else: # value is not a duplicate so mark it as having been seen and increment to the next node
			nodeDict[temp_node.val] = 1  
			temp_node = temp_node.next
	return head

def removeNode(node):
	nextNode = node.next
	node.next = nextNode.next
	node.val = nextNode.val
	