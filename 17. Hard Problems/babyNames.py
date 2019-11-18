# Each year, the government releases a list of the 10000 most common baby names
# and their frequencies (the number of babies with that name). The only problem with this is that
# some names have multiple spellings. For example, "John" and ''.Jon" are essentially the same name
# but would be listed separately in the list. Given two lists, one of names/frequencies and the other
# of pairs of equivalent names, write an algorithm to print a new list of the true frequency of each
# name. Note that if John and Jon are synonyms, and Jon and Johnny are synonyms, then John and
# Johnny are synonyms. (It is both transitive and symmetric.) In the final list, any name can be used
# as the "real" name.
# EXAMPLE
# Input:
# Names: John (15), Jon (12), Chris (13), Kris (4), Christopher (19)
# Synonyms: (Jon, John), (John, Johnny), (Chris, Kris), (Chris, Christopher)
# Output: John (27), Kris (36) 

class Queue:

	def __init__(self):
		self.queue = []

	def enqueue(self, num):
		self.queue.insert(0, num)

	def deqeue(self):
		return self.queue.pop()

	def isEmpty(self):
		return len(self.queue) == 0

def babyNames(freqs, pairs):
	graph = createGraph(pairs) # creates a graph where each synonym has an edge to all of its other synonyms
	name_map = traverseGraph(graph, freqs) # performs a bfs on the graph that maps each synonym to one name
	result = {}
	for name, count in freqs: # iterates through each name and sums the counts for each group of synonyms
		mapped_name = name_map[name]
		if mapped_name not in result:
			result[mapped_name] = 0
		result[mapped_name] += int(count)
	return result


				 
def traverseGraph(graph, freqs):
	visited = set()
	name_map = {}
	for name, count in freqs:
		if name not in visited:
			queue = Queue()
			queue.enqueue(name)
			while not queue.isEmpty(): # traverses all synonyms related to the starting point of the current iteration of the bfs
				deq_name = queue.deqeue()
				visited.add(deq_name)
				name_map[deq_name] = name # maps all synonyms to the just one name(the starting point)
				for next_name in graph[deq_name]:
					if next_name not in visited:
						queue.enqueue(next_name)
	return name_map


def createGraph(pairs): # creates a graph where each synonym has an edge to all of its other synonyms
	graph = {}
	for name1,name2 in pairs:
		if name1 not in graph:
			graph[name1] = set()
		if name2 not in graph:
			graph[name2] = set()
		graph[name1].add(name2)
		graph[name2].add(name1)
	return graph

