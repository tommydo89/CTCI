# Numbers are randomly generated and passed to a method. Write a program
# to find and maintain the median value as new values are generated.


# important concept: If we have a two heaps where the max heap contains all numbers less than the median and the min heap contains all numbers greater
# then the median then the average of the root of the two heaps will be the median value if they are the same size. If they are not equal size, then
# it is just the root of the max heap so long as we make the effort to always keep the max heap larger 

class continuousMedian:

	def __init__(self):
		self.max_heap = []
		self.min_heap = []
		self.median = None


	def insert(self, number): 
		if self.median == None: # initialization on first insert
			self.insertMaxHeap(number)
			self.median = number
		elif number <= self.median: # insert on max heap if number is less than median
			if not self.sameSize(): # if not same size, that means the max heap is larger by 1 so we need to balance it out before inserting an element into it
				removed = self.max_heap[0]
				self.insertMinHeap(removed)
				self.max_heap = self.max_heap[1:]
			self.insertMaxHeap(number) # if they are same size, we can just insert into max heap 
		else: # insert on min heap if number is greater than median
			if self.sameSize(): # if they are the same size, we must move the root of the min heap to the max heap so that when we insert into the min heap the max heap size will be larger by 1 and therefore contain the median
				removed = self.min_heap[0]
				self.insertMaxHeap(removed)
				self.min_heap = self.min_heap[1:]
			self.insertMinHeap(number)
		self.updateMedian() # after we insert we must update the median 



	def insertMaxHeap(self, number): # inserts a number into the max heap
		self.max_heap.append(number)
		curr_index = len(self.max_heap) - 1
		parent = self.getParent(curr_index, self.max_heap)
		while (curr_index > 0 and number > parent):
			self.swap(curr_index, self.max_heap)
			curr_index = (curr_index + 1) // 2 - 1
			parent = self.getParent(curr_index, self.max_heap)

	def insertMinHeap(self, number): # inserts a number into min heap
		self.min_heap.append(number)
		curr_index = len(self.min_heap) - 1
		parent = self.getParent(curr_index, self.min_heap)
		while (curr_index > 0 and number < parent):
			self.swap(curr_index, self.max_heap)
			curr_index = (curr_index + 1) // 2 - 1
			parent = self.getParent(curr_index, self.min_heap)

	def getParent(self, index, heap): # gets the value of the parent of the current node
		if index > 0:
			return heap[(index + 1) // 2 - 1]

	def swap(self, index, heap): # swaps the current node with its parent node
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