# Numbers are randomly generated and passed to a method. Write a program
# to find and maintain the median value as new values are generated.

class continuousMedian:

	def __init__(self):
		self.max_heap = []
		self.min_heap = []
		self.median = None


	def insert(self, number): 
		if self.median == None:
			self.insertMaxHeap(number)
			self.median = number
		elif number <= self.median:
			if not self.sameSize():
				removed = self.max_heap[0]
				self.insertMinHeap(removed)
				self.max_heap = self.max_heap[1:]
			self.insertMaxHeap(number)
		else:
			if self.sameSize():
				removed = self.min_heap[0]
				self.insertMaxHeap(removed)
				self.min_heap = self.min_heap[1:]
			self.insertMinHeap(number)
		self.updateMedian()



	def insertMaxHeap(self, number):
		self.max_heap.append(number)
		curr_index = len(self.max_heap) - 1
		parent = self.getParent(curr_index, self.max_heap)
		while (curr_index > 0 and number > parent):
			self.swap(curr_index, self.max_heap)
			curr_index = (curr_index + 1) // 2 - 1
			parent = self.getParent(curr_index, self.max_heap)

	def insertMinHeap(self, number):
		self.min_heap.append(number)
		curr_index = len(self.min_heap) - 1
		parent = self.getParent(curr_index, self.min_heap)
		while (curr_index > 0 and number < parent):
			self.swap(curr_index, self.max_heap)
			curr_index = (curr_index + 1) // 2 - 1
			parent = self.getParent(curr_index, self.min_heap)

	def getParent(self, index, heap):
		if index > 0:
			return heap[(index + 1) // 2 - 1]

	def swap(self, index, heap):
		parent_index = (index + 1) // 2 - 1
		temp = heap[parent_index]
		heap[parent_index] = heap[index]
		heap[index] = temp

	def sameSize(self):
		return len(self.max_heap) == len(self.min_heap)



	def updateMedian(self):
		if self.sameSize():
			self.median = (self.max_heap[0] + self.min_heap[0]) / 2
		else:
			self.median = self.max_heap[0]

	def getMedian(self):
		if self.median != None:
			return self.median
		return False