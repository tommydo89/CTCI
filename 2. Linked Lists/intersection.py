# Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. 
# Note that the intersection is defined based on reference, not value. That is, if the kth node of the 
# first linked list is the exact same node (by reference) as the jth node of the second linked list, 
# then they are intersecting.

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

#LinkedList 1
Node1 = Node(1)
Node2 = Node(2) #Intersecting Node
Node3 = Node(3)
Node1.next = Node2
Node2.next = Node3

#LinkedList 2
Node4 = Node(4)
Node5 = Node(5)
Node4.next = Node5
Node5.next = Node2


def intersection(LL1, LL2):
	while (LL1.next != None or LL2.next != None):
		if (LL1.next != None):
			LL1 = LL1.next
		if (LL2.next != None):
			LL2 = LL2.next
	if (LL1 != LL2):
		return False
	return True 

