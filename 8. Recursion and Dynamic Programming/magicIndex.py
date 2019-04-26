def magicIndex(array):
	return findMagicIndex(array, 0)


def findMagicIndex(array, index):
	if ( index == len(array) or array[index] > index): # return false if we reach the end of the array or the integer at that index is greater than the index which means it is no longer possible for an index to be equal to its integer since the array is sorted and distinct
		return False
	if (array[index] == index): # return the magic index when it is found
		return index
	return findMagicIndex(array, index + 1)
