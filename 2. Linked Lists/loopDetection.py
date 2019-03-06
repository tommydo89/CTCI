# Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop. 

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

NodeA = Node('A')
NodeB = Node('B') # beginning of the loop
NodeC = Node('C')
NodeD = Node('D')

NodeA.next = NodeB
NodeB.next = NodeC
NodeC.next = NodeD
NodeD.next = NodeB

def loopDetection(node):
	nodeDict = {}
	while (node != None):
		if (nodeDict.get(node, 0) == 1):
			return node
		else:
			nodeDict[node] = 1
		node = node.next
	return False