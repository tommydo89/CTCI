#  Design and build a "least recently used" cache, which evicts the least recently used
# item. The cache should map from keys to values (allowing you to insert and retrieve a value associated with a particular key) and be initialized with a max size. When it is full, it should evict the least
# recently used item. 

class Node:

	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.next = None
		self.prev = None


class LRU:

	def __init__(self, size):
		self.max_size = size # max size of the cache
		self.size = 0 # current size of the cache
		self.last = None # least recently used node
		self.head = None # most recently used node
		self.map = {} # maps each key to a node that stores the key,val pair

	# adds an item to the cache
	def add(self, key, value):
		new_Node = Node(key, value)
		if self.isFull(): # if cache is full, remove the least recently used
			self.removeLast()
		if self.last == None:
			self.last = new_Node
		if self.head != None: 
			self.head.prev = new_Node
		new_Node.next = self.head
		self.head = new_Node
		self.map[key] = new_Node
		self.size += 1

	# removes the least recently used node when the cache is full
	def removeLast(self):
		if self.isEmpty():
			return False
		key = self.last.key
		self.last = self.last.prev
		if self.last != None: # last will be None if there was only 1 item in the cache and so we want to avoid referencing a None object
			self.last.next = None
		self.size -= 1
		del self.map[key]

	# moves a node to the front after it has been accessed
	def moveToFront(self, key):
		node = self.map[key]
		if node != self.head: # if the node is already at the front, we do not need to do anything

			# unlinks the node in a specific manner depending on whether or not it is the last node
			if node == self.last:
				self.last = node.prev
				self.last.next = None
			else:
				node.prev.next = node.next

			# moves the node to the head of the linked list
			node.next = self.head
			self.head = node


	def isFull(self):
		return self.size == self.max_size

	def isEmpty(self):
		return self.size == 0

	# retrieves the value associated with a key and then also moves its associated node to the front
	def retrieve(self, key):
		if key not in self.map:
			return False
		else:
			self.moveToFront(key)
			return self.map[key].val
