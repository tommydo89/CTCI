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

def removeDups(head):
	thisdict = {}
	temp_head = head
	thisdict[temp_head.val] = thisdict.get(temp_head.val, 0) + 1
	while (temp_head.next != None):
		if (thisdict.get(temp_head.val, 0) > 0):
			temp_head.next = temp_head.next.next
		else:
			thisdict[temp_head.val] = thisdict.get(temp_head.val, 0) + 1
		temp_head = temp_head.next
	return head
	