# You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list. 

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

# LinkedList 1
Node1 = Node(0)
Node2 = Node(0)
Node3 = Node(1)
Node1.next = Node2
Node2.next = Node3

# LinkedList 2
Node4 = Node(0)
Node5 = Node(2)
Node4.next = Node5


def sumLists(LinkedList1, LinkedList2):
	factor = 1
	total = 0
	while (LinkedList1 != None or LinkedList2 != None):
		if (LinkedList1 != None):
			total += LinkedList1.val * factor
			LinkedList1 = LinkedList1.next
		if (LinkedList2 != None):
			total += LinkedList2.val * factor
			LinkedList2 = LinkedList2.next
		factor *= 10
	returnNode = Node(None)
	temp = returnNode
	total_str = str(total)
	for index in range(len(total_str)-1, -1, -1):
		digit = int(total_str[index])
		if (temp.val == None):
			temp.val = digit
		else:
			newNode = Node(digit)
			temp.next = newNode
			temp = temp.next
	return returnNode

