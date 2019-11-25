 # Design an algorithm to find the smallest K numbers in an array. 

def smallestK(arr, k):
	arr.sort()
	return arr[:k]