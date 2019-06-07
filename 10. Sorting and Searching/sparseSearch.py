# Given a sorted array of strings that is interspersed with empty strings, write a
# method to find the location of a given string. 

def sparseSearch(array, string):
	low = 0
	high = len(array) - 1
	mid = (low + high) // 2
	return recursiveSearch(array, string, low, mid, high)


def recursiveSearch(array, string, low, mid, high):
	if array[low] == string:
		return low
	if array[mid] == string:
		return mid
	if array[high] == string:
		return high
	if len(array[mid]) == 0: # the element at this index is an empty string, so we must find the next index that actually has a word
		next_index = findNext(mid + 1, array)
		if (array[next_index] == string):
			return next_index
		if (string < array[next_index]): # if the string is less than the next word, then recurse on the lower half
			return recursiveSearch(array, string, low + 1, (low+mid)//2, mid - 1) 
		else: # else recurse on everything after the next_index that we calculated
			return recursiveSearch(array, string, next_index + 1, (next_index + high)//2, high - 1)

def findNext(index, array): # finds the index of the next element that is not an empty string
	while (len(array[index]) == 0):
		index += 1
	return index