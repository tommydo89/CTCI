# You are given an array like data structure Listy which lacks a size
# method. It does, however, have an elementAt ( i) method that returns the element at index i in
# 0( 1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data
# structure only supports positive integers.) Given a Li sty which contains sorted, positive integers,
# find the index at which an element x occurs. If x occurs multiple times, you may return any index. 

def sortedSearch(array, target):
	high = 0 
	while (elementAt(high, array) != -1 and array[high] < target): # find either the max index of the array or an index that is out of bounds
		if high == 0:
			high += 2
		else:
			high *= 2
	low = 0
	mid = (low+high)//2
	return recursiveSearch(array, target, low, mid, high)


def recursiveSearch(array, target, low , mid, high):
	if elementAt(low, array) == target:
		return low
	if elementAt(mid, array) == target:
		return mid
	if elementAt(high, array) == target:
		return high
	if elementAt(mid, array) == -1 or target < elementAt(mid, array): # recurse on the left if the target is less than the mid, or if elementAt(mid,array) returns -1 which means the index is too high
		return recursiveSearch(array, target, low+1, (low+mid)//2, mid-1)
	else: # else recurse on the right
		return recursiveSearch(array, target, mid+1, (mid+high)//2, high-1)


def elementAt(index, array): # returns the element at the specified index or returns -1 if the index is out of bounds
	max_index = len(array) - 1
	if (index > max_index):
		return -1
	return array[index]