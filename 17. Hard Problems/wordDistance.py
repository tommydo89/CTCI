# You have a large text file containing words. Given any two words, find the shortest
# distance (in terms of number of words) between them in the file. If the operation will be repeated
# many times for the same file (but different pairs of words), can you optimize your solution? 

def wordDistance(file, word1, word2):
	shortest = None
	location1 = None
	location2 = None
	index = 0
	for word in file:
		if word == word1:
			location1 = index
		elif word == word2:
			location2 = index
		# update shortest if shortest is still None after having found both words or if the current locations are shorter than the previous
		if location1 != None and location2 != None and (shortest == None or abs(location1-location2) < shortest):
				shortest = abs(location1-location2) - 1
		index += 1
	return shortest